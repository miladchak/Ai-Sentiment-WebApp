// script.js

document.addEventListener('DOMContentLoaded', () => {
    const inputTextElement = document.getElementById('inputText');
    const analyzeButtonElement = document.getElementById('analyzeButton');
    const resultElement = document.getElementById('result');
    const sentimentResultElement = document.getElementById('sentimentResult');
    const themeToggleElement = document.getElementById('themeToggle'); // Get theme toggle button
    const themeIcon = themeToggleElement.querySelector('i'); // Get theme icon inside button

    // Function to set theme based on localStorage or default to light
    function setTheme(themeName) {
        localStorage.setItem('theme', themeName);
        document.body.className = themeName;
        updateThemeIcon(themeName); // Update icon when theme is set
    }

    // Function to toggle between light and dark theme
    function toggleTheme() {
        if (localStorage.getItem('theme') === 'dark-theme') {
            setTheme('light-theme');
        } else {
            setTheme('dark-theme');
        }
    }

    // Function to update theme icon based on current theme
    function updateThemeIcon(themeName) {
        if (themeName === 'dark-theme') {
            themeIcon.classList.remove('fa-moon');
            themeIcon.classList.add('fa-sun'); // Change to sun icon for dark theme
        } else {
            themeIcon.classList.remove('fa-sun');
            themeIcon.classList.add('fa-moon'); // Change to moon icon for light theme
        }
    }


    // Immediately check and apply stored theme on page load
    const storedTheme = localStorage.getItem('theme');
    if (storedTheme) {
        setTheme(storedTheme);
    } else {
        setTheme('light-theme'); // Default to light theme if no theme in localStorage
    }


    // Event listener for theme toggle button
    themeToggleElement.addEventListener('click', toggleTheme);


    analyzeButtonElement.addEventListener('click', async () => {
        const text = inputTextElement.value;

        if (!text.trim()) {
            alert('Please enter text for analysis.');
            return;
        }

        console.log('DEBUG (Frontend): Before sending request to backend...');

        try {
            const response = await fetch('/analyze_sentiment', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ text })
            });

            console.log('DEBUG (Frontend): Response received from backend:', response);

            if (!response.ok) {
                console.error('DEBUG (Frontend): Unsuccessful response from backend:', response.status, response.statusText);
                throw new Error(`Request error: ${response.status} ${response.statusText}`);
            }

            const data = await response.json();
            console.log('DEBUG (Frontend): JSON data from response:', data);

            sentimentResultElement.textContent = `Text Sentiment: ${data.sentiment}`;
            resultElement.classList.remove('hidden');

        } catch (error) {
            console.error('DEBUG (Frontend): Fetch error in frontend:', error);
            sentimentResultElement.textContent = 'Sorry, an error occurred during sentiment analysis.';
            resultElement.classList.remove('hidden');
        }
    });
});