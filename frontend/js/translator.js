// Translation functionality for a language-switching application.

// This object will hold the translations.
let translations = {};

// Load translations from a JSON file.
function loadTranslations(url) {
    return fetch(url)
        .then(response => response.json())
        .then(data => {
            translations = data;
        })
        .catch(error => console.error('Error loading translations:', error));
}

// Function to switch language.
function switchLanguage(language) {
    if (!translations[language]) {
        console.error('Language not available:', language);
        return;
    }
    const elementsToTranslate = document.querySelectorAll('[data-translate]');
    elementsToTranslate.forEach(element => {
        const key = element.getAttribute('data-translate');
        element.innerText = translations[language][key] || key;
    });
}

// Example usage:
// Load the translations when the document is ready.
document.addEventListener('DOMContentLoaded', () => {
    loadTranslations('path/to/your/translations.json') // specify the path to your JSON file
        .then(() => {
            // Set default language
            switchLanguage('en');
        });
});

// HTML Example:
// <h1 data-translate='welcome'>Welcome</h1>
// <button onclick="switchLanguage('es')">Switch to Spanish</button}

