const express = require("express");
const bodyParser = require("body-parser");
const axios = require("axios");

const app = express();
app.set("view engine", "ejs");

app.use(bodyParser.urlencoded({ extended: true }));

app.get("/", (req, res) => {
  res.render("index");
});

app.post("/submit", async (req, res) => {
  try {
    const response = await axios.post(
      "http://backend:5000/submit",
      req.body
    );
    res.send(`<h2>${response.data.message}</h2>`);
  } catch (err) {
    res.send("Backend not responding 😐");
  }
});

app.listen(3000, () => {
  console.log("Frontend running on port 3000");
});
