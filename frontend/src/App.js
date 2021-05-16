import logo from './logo.svg';
import './App.css';
import VideoGrid from './Components/VideoGridComponent'
import Header from './Components/Header'
import { useState } from 'react';
import Navigation from './Components/Navigation'

function App() {
  const [token, setToken] = useState(localStorage.getItem('BetterTube_auth_token'));
  return (
    <div className="App">
      <Header token={token} setToken={setToken}/>
      <Navigation />
      <VideoGrid token={token}/>
    </div>
  );
}

export default App;
