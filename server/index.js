const express = require("express")

const PORT = process.env.PORT || 3001;

const app = express();

// creating React endpoint

app.get("/api", (req, res) => {
    res.json({ message: "This shit works" });
  });

app.listen(PORT, ()=> {
    console.log(`Server listening on ${PORT}`);
});
