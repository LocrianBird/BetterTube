import React from 'react';
import '../ComponentStyle/navigation.css'
import Home from '../ComponentStyle/img/home.png'
import Favorite from '../ComponentStyle/img/favorite.png'
import Music from '../ComponentStyle/img/music.png'
import Playlist from '../ComponentStyle/img/playlist.png'
import Arrow from '../ComponentStyle/img/arrow.png'
import Settings from '../ComponentStyle/img/settings.png'

class Navigation extends React.Component {
  constructor(props) {
    super(props);
  }

  render(){
    return(
      <nav className="navbar">
          <ul className="navbar-nav">
            
            <li className="nav-item">
              <a href="#" className="nav-link">
                <img src={Home} width="30px"/>
                <span className="link-text">Home</span>
              </a>
            </li>

            <li className="nav-item">
              <a href="#" className="nav-link">
                <img src={Favorite} width="30px"/>
                <span className="link-text">Favorite</span>
              </a>
            </li>

            <li className="nav-item">
              <a href="#" className="nav-link">
                <img src={Music} width="30px"/>
                <span className="link-text">Music</span>
              </a>
            </li>

            <li className="nav-item">
              <a href="#" className="nav-link">
                <img src={Playlist} width="30px"/>
                <span className="link-text">Playlist</span>
              </a>
            </li>

            <li className="nav-item">
              <a href="#" className="nav-link">
                <img src={Settings} width="30px"/>
                <span className="link-text">Settings</span>
              </a>
            </li>
          </ul>
      </nav>
    )
  }

}

export default Navigation;