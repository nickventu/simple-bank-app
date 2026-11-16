import { useState } from "react";
import { useParams, useNavigate, Link } from "react-router-dom";
import { apiFetch } from "../api";

function Deposit() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [amount, setAmount] = useState("");
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState(null);

  async function handleSubmit(e) {
    e.preventDefault();
    setSubmitting(true);
    setError(null);

    try {
      const res = await apiFetch(`/api/accounts/${id}/deposit`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ amount: Number(amount) }),
      });
      if (!res.ok) {
        const body = await res.json().catch(() => null);
        throw new Error(body?.detail ?? `Request failed: ${res.status}`);
      }
      navigate(`/accounts/${id}`);
    } catch (err) {
      setError(err.message);
    } finally {
      setSubmitting(false);
    }
  }

  return (
    <div>
      <h1>Deposit</h1>
      <form onSubmit={handleSubmit}>
        <label htmlFor="amount">Amount</label>
        <input
          id="amount"
          type="number"
          min="0"
          step="0.01"
          value={amount}
          onChange={(e) => setAmount(e.target.value)}
          required
        />

        {error && <p style={{ color: "red" }}>{error}</p>}

        <button type="submit" disabled={submitting}>
          {submitting ? "Depositing..." : "Deposit"}
        </button>
      </form>

      <Link to={`/accounts/${id}`}>Back to account</Link>
    </div>
  );
}

export default Deposit;
