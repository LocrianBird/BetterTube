import React  from 'react';
import '../ComponentStyle/header.css';
import BetterTubeLogo from '../ComponentStyle/img/BetterTubeLogo.png';
import SearchLogo from '../ComponentStyle/img/search.png';
import Auth from './Auth'
import MenuBtn1 from '../ComponentStyle/img/more_inactive.png'


class Header extends React.Component {
  constructor(props) {
    super(props);

  }

  render(){
    return(
      <div className="header">
        {/* <button className="menu-btn">
          <img src={MenuBtn1} height="25px"/>
        </button> */}
        <img src={BetterTubeLogo} alt="BetterTube Logo" className="logo">
        </img>
        <form className="input-group">
          <input type="search" name="search" className="input-search" placeholder="Search" />
          <button type="submit" className="button-search">
            <img src={SearchLogo} alt="search logo"className="icon icon-search" width="19" height="19"/> 
          </button>
        </form>
        <Auth token={this.props.token} setToken={this.props.setToken}/>
      </div>
    )
  }
}

export default Header;