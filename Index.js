// index.js: Main entry point for the platform

const express = require("express");
const bodyParser = require("body-parser");
require("dotenv").config(); // Load .env variables

const { replicateTask, processPayment, generateAIResult } = require("./services/tasks");

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to parse incoming JSON data
app.use(bodyParser.json());

// Route: Home
app.get("/", (req, res) => {
  res.send("Welcome to the AI-Powered Dynex Integration Platform!");
});

// Route: Replicate Task
app.post("/api/replicate", (req, res) => {
  try {
    const taskData = req.body;
    const replicated = replicateTask(taskData);
    res.status(200).json({ success: true, data: replicated });
  } catch (error) {
    res.status(500).json({ success: false, error: error.message });
  }
});

// Route: Process Payment
app.post("/api/payment", (req, res) => {
  try {
    const paymentInfo = req.body;
    const response = processPayment(paymentInfo);
    res.status(200).json({ success: true, data: response });
  } catch (error) {
    res.status(500).json({ success: false, error: error.message });
  }
});

// Route: Generate AI Result
app.post("/api/ai", (req, res) => {
  try {
    const inputData = req.body;
    const result = generateAIResult(inputData);
    res.status(200).json({ success: true, data: result });
  } catch (error) {
    res.status(500).json({ success: false, error: error.message });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
