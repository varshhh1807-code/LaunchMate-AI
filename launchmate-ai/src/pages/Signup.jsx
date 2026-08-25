import "./Login.css";
import { Link } from "react-router-dom";
import { useState } from "react";


function Signup() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSignup = async () => {
  try {
    const response = await fetch("http://127.0.0.1:8000/signup", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        username: email,
        password: password,
      }),
    });

    const data = await response.json();

    alert(data.message);

  } catch (error) {
    alert("Server Error");
    console.log(error);
  }
};

  return (
    <div className="login-container">
      <div className="login-box">

        <div className="title">LaunchMate AI</div>
        <div className="subtitle">Your Intelligent Startup Co-Founder</div>

        <img
          className="user-icon"
          src="https://cdn-icons-png.flaticon.com/512/149/149071.png"
          alt="User"
        />

        <h2>Create Account</h2>

        <label>Full Name</label>
        <input
          type="text"
          placeholder="Enter your name"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />

        <label>Email</label>
        <input
          type="email"
          placeholder="Enter your email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />

        <label>Password</label>
        <input
          type="password"
          placeholder="Enter your password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />

        <label className="checkbox">
          <input type="checkbox" />
          I Agree to the Terms & Privacy Policy
        </label>

        <button onClick={handleSignup}>
          Create Account
        </button>

        <p>Already have an account?</p>

        <Link to="/">Login</Link>

      </div>
    </div>
  );
}

export default Signup;