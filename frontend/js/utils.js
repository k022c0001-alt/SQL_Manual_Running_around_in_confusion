// Utility functions for JavaScript

/**
 * Get current date and time in YYYY-MM-DD HH:MM:SS format.
 * @returns {string} Current date and time.
 */
function getCurrentDateTime() {
    const now = new Date();
    return now.toISOString().slice(0, 19).replace('T', ' ');
}

/**
 * Generate a random number between min and max.
 * @param {number} min - Minimum value.
 * @param {number} max - Maximum value.
 * @returns {number} Random number between min and max.
 */
function getRandomNumber(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

/**
 * Array of unique values.
 * @param {Array} arr - The input array.
 * @returns {Array} Array of unique values.
 */
function uniqueArray(arr) {
    return [...new Set(arr)];
}

// Export utility functions
export { getCurrentDateTime, getRandomNumber, uniqueArray };