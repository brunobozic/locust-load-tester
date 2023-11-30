const express = require('express');
const jwt = require('jsonwebtoken');
const app = express();
const port = 3000;

// Middleware to parse JSON requests
app.use(express.json());

// Secret key for JWT (use a more secure key in a real application)
const jwtSecret = 'your-secret-key';

// Mock login endpoint
app.post('/login', (req, res) => {
    // Create a fake JWT token
    const token = jwt.sign({ username: req.body.username }, jwtSecret, { expiresIn: '1h' });

    res.json({ jwtToken: token });
});

// Mock register endpoint
app.post('/register', (req, res) => {
    // Generate a fake UserDto response
    const userDto = {
        ActiveTo: new Date().toISOString(),
        Email: req.body.email || "test@example.com",
        HasBeenVerified: new Date(),
        Id: Math.floor(Math.random() * 10000),
        Status: "Active",
        UserName: req.body.userName || "testuser",
        UserRoles: ["User"]
    };

    res.status(201).json(userDto);
});

app.listen(port, () => {
    console.log(`Mock server listening at http://localhost:${port}`);
});
