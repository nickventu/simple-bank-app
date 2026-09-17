import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";

function AccountDetails() {
  const { id } = useParams();
  const [account, setAccount] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    let cancelled = false;

    async function fetchAccount() {
      setLoading(true);
      setError(null);
      try {
        const res = await fetch(`/api/accounts/${id}`);
        if (!res.ok) throw new Error(`Request failed: ${res.status}`);
        const data = await res.json();
        if (!cancelled) setAccount(data);
      } catch (err) {
        if (!cancelled) setError(err.message);
      } finally {
        if (!cancelled) setLoading(false);
      }
    }

    fetchAccount();
    return () => {
      cancelled = true;
    };
  }, [id]);

  if (loading) return <div>Loading account...</div>;
  if (error) return <div>Error loading account: {error}</div>;
  if (!account) return null;

  return (
    <div>
      <h1>Account {account.accountId}</h1>
      <p>Owner: {account.userName}</p>
      <p>Balance: ${account.balance}</p>

      <nav>
        <Link to={`/accounts/${id}/deposit`}>Deposit</Link>{" | "}
        <Link to={`/accounts/${id}/withdraw`}>Withdraw</Link>{" | "}
        <Link to={`/accounts/${id}/transactions`}>Transaction History</Link>
      </nav>
    </div>
  );
}

export default AccountDetails;
