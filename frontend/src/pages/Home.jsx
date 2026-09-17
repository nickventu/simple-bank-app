import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";

function Home() {
  const [accountId, setAccountId] = useState("");
  const navigate = useNavigate();

  function handleLookup(e) {
    e.preventDefault();
    const trimmed = accountId.trim();
    if (trimmed) navigate(`/accounts/${trimmed}`);
  }

  return (
    <div>
      <h1>Bank App</h1>
      <Link to="/create-account">Create Account</Link>

      <form onSubmit={handleLookup}>
        <label htmlFor="accountId">Go to account</label>
        <input
          id="accountId"
          type="text"
          value={accountId}
          onChange={(e) => setAccountId(e.target.value)}
          placeholder="Account ID"
        />
        <button type="submit">View</button>
      </form>
    </div>
  );
}

export default Home;
