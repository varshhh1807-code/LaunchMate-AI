import "./Login.css";
import { Link } from "react-router-dom";
import { useState } from "react";
import { useNavigate } from "react-router-dom";
function Login() {
const [email, setEmail] = useState("");
const [password, setPassword] = useState("");
const navigate = useNavigate();

const handleLogin = async () => {
  try {
    const response = await fetch("http://127.0.0.1:8000/login", {
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

    if (data.message === "Login Successful") {
      alert("Login Successful!");
      navigate("/dashboard");
    } else {
      alert(data.message);
    }
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
        

        <h2>Login</h2>

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

        <p className="forgot">Forgot Password?</p>

        <button onClick={handleLogin}>
        Login
        </button>

        <div className="divider">OR</div>

        <p>Don't have an account?</p>

        <Link to="/signup">Sign Up</Link>

      </div>
    </div>
  );
}

export default Login;