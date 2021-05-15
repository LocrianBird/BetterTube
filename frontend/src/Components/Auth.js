import React from 'react';
import Avatar from '../ComponentStyle/img/avatar.png';
import '../ComponentStyle/Header.css';
import Loader from 'react-loader-spinner';
import axios from 'axios';

class Auth extends React.Component {
  Type = Object.freeze({'NOT_LOGGED_IN': 0, 'LOADING': 1, 'LOGGED_IN': 2});
  constructor(props){
    super(props);
    this.state = {
      type: this.Type.LOADING,
      user: null,
    }
  }
  

  componentDidMount(){
    axios.get(window.location.origin + '/get_user_data')
    .then(res=>{
      console.log(res.data);
      this.setState({
        user: res.data,
        type: this.Type.LOGGED_IN 
      })
    })
    .catch(err=>{
      this.setState({
        type: this.Type.NOT_LOGGED_IN 
      })
    })
  }

  
  onSigninClicked() {
    this.setState({
      type: this.Type.LOADING
    })
    axios.get(window.location.origin + '/request_authorization_url')
    .then(res=>{
      window.location = res.data.authorization_url;
    })
    .catch(err=>{
      console.log(err);
    })
  }


  renderByType(type){
    switch(type) {
      case this.Type.LOGGED_IN: 
        return(
          <div className="auth">
            <img src={this.state.user.avatar} alt={this.state.user.name} className="user-avatar" />
            <p className="user-name">{this.state.user.name}</p>
        </div>
      )
      case this.Type.NOT_LOGGED_IN:
        return(
          <div className="auth">
            <button onClick={this.onSigninClicked.bind(this)} className="auth-btn">Sign In</button>
        </div>
      )
      case this.Type.LOADING:
        return(
          <div className="auth spinner">
            <Loader 
              type="Puff"
              color="#e2a917"
              height={30}
              width={30}
            />
          </div>
        )
    }
  }


  render(){
    return (this.renderByType(this.state.type));
  }
}

export default Auth;