const express = require('express');
const axios = require('axios');
const path = require('path');
const app = express();
app.use(express.json());

// Base URL for the Flask API
const flaskBaseURL = 'http://127.0.0.1:5000';

// Serve the specific `styles.css` file
app.use('/styles.css', express.static(path.join(__dirname, 'styles.css')));

// Set EJS as the view engine
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// Render home page
app.get('/', (req, res) => {
    res.render('index');
});

// Investor CRUD operations

// Create Investor
app.post('/investor', async (req, res) => {
    try {
        const response = await axios.post(`${flaskBaseURL}/investor`, req.body);
        res.status(response.status).send(response.data);
    } catch (error) {
        res.status(error.response?.status || 500).send(error.response?.data || { error: 'Error creating investor' });
    }
});

// Update Investor
app.put('/investor/:id', async (req, res) => {
    try {
        const response = await axios.put(`${flaskBaseURL}/investor/${req.params.id}`, req.body);
        res.status(response.status).send(response.data);
    } catch (error) {
        res.status(error.response?.status || 500).send(error.response?.data || { error: 'Error updating investor' });
    }
});

// Delete Investor
app.delete('/investor/:id', async (req, res) => {
    try {
        const response = await axios.delete(`${flaskBaseURL}/investor/${req.params.id}`);
        res.status(response.status).send(response.data);
    } catch (error) {
        res.status(error.response?.status || 500).send(error.response?.data || { error: 'Error deleting investor' });
    }
});

// Get Investor
app.get('/investor/:id', async (req, res) => {
    try {
        const response = await axios.get(`${flaskBaseURL}/investor/${req.params.id}`);
        res.status(response.status).send(response.data);
    } catch (error) {
        res.status(error.response?.status || 500).send(error.response?.data || { error: 'Error fetching investor' });
    }
});

// Get Investor Portfolio
app.get('/investor/:id/portfolio', async (req, res) => {
    try {
        const response = await axios.get(`${flaskBaseURL}/investor/${req.params.id}/portfolio`);
        res.status(response.status).send(response.data);
    } catch (error) {
        res.status(error.response?.status || 500).send(error.response?.data || { error: 'Error fetching portfolio' });
    }
});

// Stock CRUD operations

// Create Stock
app.post('/stock', async (req, res) => {
    try {
        const response = await axios.post(`${flaskBaseURL}/stock`, req.body);
        res.status(response.status).send(response.data);
    } catch (error) {
        res.status(error.response?.status || 500).send(error.response?.data || { error: 'Error creating stock' });
    }
});

// Update Stock
app.put('/stock/:id', async (req, res) => {
    try {
        const response = await axios.put(`${flaskBaseURL}/stock/${req.params.id}`, req.body);
        res.status(response.status).send(response.data);
    } catch (error) {
        res.status(error.response?.status || 500).send(error.response?.data || { error: 'Error updating stock' });
    }
});

// Delete Stock
app.delete('/stock/:id', async (req, res) => {
    try {
        const response = await axios.delete(`${flaskBaseURL}/stock/${req.params.id}`);
        res.status(response.status).send(response.data);
    } catch (error) {
        res.status(error.response?.status || 500).send(error.response?.data || { error: 'Error deleting stock' });
    }
});

// Bond CRUD operations

// Create Bond
app.post('/bond', async (req, res) => {
    try {
        const response = await axios.post(`${flaskBaseURL}/bond`, req.body);
        res.status(response.status).send(response.data);
    } catch (error) {
        res.status(error.response?.status || 500).send(error.response?.data || { error: 'Error creating bond' });
    }
});

// Update Bond
app.put('/bond/:id', async (req, res) => {
    try {
        const response = await axios.put(`${flaskBaseURL}/bond/${req.params.id}`, req.body);
        res.status(response.status).send(response.data);
    } catch (error) {
        res.status(error.response?.status || 500).send(error.response?.data || { error: 'Error updating bond' });
    }
});

// Delete Bond
app.delete('/bond/:id', async (req, res) => {
    try {
        const response = await axios.delete(`${flaskBaseURL}/bond/${req.params.id}`);
        res.status(response.status).send(response.data);
    } catch (error) {
        res.status(error.response?.status || 500).send(error.response?.data || { error: 'Error deleting bond' });
    }
});

// Transactions

// Stock Transaction
app.post('/investor/:id/transaction/stock', async (req, res) => {
    try {
        const response = await axios.post(`${flaskBaseURL}/investor/${req.params.id}/transaction/stock`, req.body);
        res.status(response.status).send(response.data);
    } catch (error) {
        res.status(error.response?.status || 500).send(error.response?.data || { error: 'Error performing stock transaction' });
    }
});

// Bond Transaction
app.post('/investor/:id/transaction/bond', async (req, res) => {
    try {
        const response = await axios.post(`${flaskBaseURL}/investor/${req.params.id}/transaction/bond`, req.body);
        res.status(response.status).send(response.data);
    } catch (error) {
        res.status(error.response?.status || 500).send(error.response?.data || { error: 'Error performing bond transaction' });
    }
});

// Delete Stock Transaction
app.delete('/transaction/stock/:transaction_id', async (req, res) => {
    try {
        const response = await axios.delete(`${flaskBaseURL}/transaction/stock/${req.params.transaction_id}`);
        res.status(response.status).send(response.data);
    } catch (error) {
        res.status(error.response?.status || 500).send(error.response?.data || { error: 'Error deleting stock transaction' });
    }
});

// Delete Bond Transaction
app.delete('/transaction/bond/:transaction_id', async (req, res) => {
    try {
        const response = await axios.delete(`${flaskBaseURL}/transaction/bond/${req.params.transaction_id}`);
        res.status(response.status).send(response.data);
    } catch (error) {
        res.status(error.response?.status || 500).send(error.response?.data || { error: 'Error deleting bond transaction' });
    }
});

// Start the server
const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
