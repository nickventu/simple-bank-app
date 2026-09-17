import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";

function TransactionHistory() {
  const { id } = useParams();
  const [transactions, setTransactions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    let cancelled = false;

    async function fetchTransactions() {
      setLoading(true);
      setError(null);
      try {
        const res = await fetch(`/api/accounts/${id}/transactions`);
        if (!res.ok) throw new Error(`Request failed: ${res.status}`);
        const data = await res.json();
        if (!cancelled) setTransactions(data);
      } catch (err) {
        if (!cancelled) setError(err.message);
      } finally {
        if (!cancelled) setLoading(false);
      }
    }

    fetchTransactions();
    return () => {
      cancelled = true;
    };
  }, [id]);

  if (loading) return <div>Loading transactions...</div>;
  if (error) return <div>Error loading transactions: {error}</div>;

  return (
    <div>
      <h1>Transaction History</h1>

      {transactions.length === 0 ? (
        <p>No transactions yet.</p>
      ) : (
        <ul>
          {transactions.map((txn, i) => (
            <li key={i}>
              {txn.type} — ${txn.amount} —{" "}
              {new Date(txn.transaction_date).toLocaleString()}
            </li>
          ))}
        </ul>
      )}

      <Link to={`/accounts/${id}`}>Back to account</Link>
    </div>
  );
}

export default TransactionHistory;
