import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import CreateAccount from "./pages/CreateAccount";
import AccountDetails from "./pages/AccountDetails";
import Deposit from "./pages/Deposit";
import Withdraw from "./pages/Withdraw";
import TransactionHistory from "./pages/TransactionHistory";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/create-account" element={<CreateAccount />} />
        <Route path="/accounts/:id" element={<AccountDetails />} />
        <Route path="/accounts/:id/deposit" element={<Deposit />} />
        <Route path="/accounts/:id/withdraw" element={<Withdraw />} />
        <Route path="/accounts/:id/transactions" element={<TransactionHistory />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;