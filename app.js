require("dotenv").config();
const express = require("express");
var nodemailer = require("nodemailer");
const { spawn } = require("child_process");
const cors = require("cors");
const fs = require("fs-extra");
const app = express();

app.use(cors());
app.use(express.json());

const port = process.env.PORT || 3001;

app.get("/", (req, res) => {
  res.send("api");
});

app.post("/submitform", (req, res) => {
  // res.sendFile(__dirname + "/greetings.html");
  const formData = JSON.stringify(req.body.inputFields);
  const email = req.body.email;
  console.log(formData);
  console.log(email);
  const transporter = nodemailer.createTransport({
    host: "smtp.gmail.com",
    port: 465,
    secure: true,
    auth: {
      type: "OAuth2",
      user: process.env.MAIL_USERNAME,
      clientId: process.env.OAUTH_CLIENTID,
      clientSecret: process.env.OAUTH_CLIENT_SECRET,
      refreshToken: process.env.OAUTH_REFRESH_TOKEN,
      accessToken: process.env.ACCESS_TOKEN,
    },
  });
  const mailOptions = {
    from: process.env.MAIL,
    to: email,
    subject: "Your mp3 file is here!",
    attachments: [
      {
        filename: "output.mp3",
        path: "output.mp3",
      },
    ],
  };
  const python = spawn("python", ["mashup.py", formData]);
  python.stderr.on("data", (data) => {
    console.error(`Python script error: ${data.toString()}`);
  });
  python.stdout.on("data", (data) => {
    mystr = data.toString();
    console.log(mystr);
  });
  python.on("close", () => {
    console.log("Python execution completed");
    const merge = spawn("python", ["merge.py", "output.mp3"]);
    merge.stderr.on("data", (data) => {
      console.error(`Python script error: ${data.toString()}`);
    });
    merge.on("close", () => {
      console.log("Python execution completed!");
      transporter.sendMail(mailOptions, (error) => {
        if (error) {
          console.log(error);
        } else {
          console.log("Mail sent!");
          fs.remove("songs");
          // fs.remove("output.mp3");
          console.log("files removed");
        }
      });
    });
  });
});

app.listen(port, () => {
  console.log("Server started on port 3001");
});
