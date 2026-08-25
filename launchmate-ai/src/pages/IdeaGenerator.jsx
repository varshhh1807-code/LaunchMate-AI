import "./IdeaGenerator.css";
import { useNavigate } from "react-router-dom";
import { useState } from "react";

function IdeaGenerator() {
  const navigate = useNavigate();

  const [idea, setIdea] = useState("");
  const [category, setCategory] = useState("Education");
  const [audience, setAudience] = useState("Students");
  const [businessModel, setBusinessModel] = useState("Freemium");
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);

  const handleGenerate = async () => {
    if (!idea.trim()) {
      alert("Please enter a startup idea");
      return;
    }

    try {
      setLoading(true);

      const topic = `${idea} | Category: ${category} | Audience: ${audience} | Business Model: ${businessModel}`;

      const response = await fetch(
        `http://127.0.0.1:8000/idea?topic=${encodeURIComponent(topic)}`
      );

      const data = await response.json();

      console.log("DATA =", data);

      if (data.error) {
        alert(data.error);
      } else {
        setResult(data.idea || "");
      }
    } catch (error) {
      console.error(error);
      alert("Failed to generate idea");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="idea-container">
      <div className="navigation-buttons">
        <button
          className="back-btn"
          onClick={() => navigate("/dashboard")}
        >
          ◀
        </button>

        <button
          className="next-btn"
          onClick={() => navigate("/market-research")}
        >
          ▶
        </button>
      </div>

      <h1>Idea Generator Agent</h1>

      <label>💡 Startup Idea</label>
      <textarea
        placeholder="Enter your startup idea..."
        value={idea}
        onChange={(e) => setIdea(e.target.value)}
      />

      <label>📂 Category</label>
      <select
        value={category}
        onChange={(e) => setCategory(e.target.value)}
      >
        <option>Education</option>
        <option>Healthcare</option>
        <option>Finance</option>
        <option>E-commerce</option>
      </select>

      <label>👥 Target Audience</label>
      <select
        value={audience}
        onChange={(e) => setAudience(e.target.value)}
      >
        <option>Students</option>
        <option>Professionals</option>
        <option>Businesses</option>
      </select>

      <label>💼 Preferred Business Model</label>
      <input
        type="text"
        value={businessModel}
        onChange={(e) => setBusinessModel(e.target.value)}
      />

      <button
        className="generate-btn"
        onClick={handleGenerate}
        disabled={loading}
      >
        {loading ? "Generating..." : "✨ Generate Idea"}
      </button>

      <div className="result-box">
        <h2>✨ AI Generated Result</h2>

        <div
          style={{
            background: "#fff",
            color: "#000",
            border: "1px solid #ccc",
            borderRadius: "10px",
            padding: "15px",
            minHeight: "400px",
            whiteSpace: "pre-wrap",
            overflowY: "auto",
          }}
        >
          {result || "Generated idea will appear here..."}
        </div>
      </div>
    </div>
  );
}

export default IdeaGenerator;