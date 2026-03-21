// api.js

/**
 * Function to fetch data from the backend API
 * @param {string} endpoint - The endpoint to send the request to
 * @param {object} options - Options for the fetch request
 * @returns {Promise<object>} - A promise that resolves to the response data
 */
async function fetchData(endpoint, options = {}) {
    const response = await fetch(endpoint, options);
    if (!response.ok) {
        throw new Error(`Error fetching data: ${response.statusText}`);
    }
    return response.json();
}

/**
 * Function to send data to the backend API
 * @param {string} endpoint - The endpoint to send the request to
 * @param {object} data - The data to be sent
 * @returns {Promise<object>} - A promise that resolves to the response data
 */
async function sendData(endpoint, data) {
    const response = await fetch(endpoint, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
    });
    if (!response.ok) {
        throw new Error(`Error sending data: ${response.statusText}`);
    }
    return response.json();
}

// Example of usage:
// fetchData('/api/example-endpoint').then(data => console.log(data));
// sendData('/api/example-endpoint', { key: 'value' }).then(data => console.log(data));
