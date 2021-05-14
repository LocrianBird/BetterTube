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
      type: props.token != null ? this.Type.LOADING : this.Type.NOT_LOGGED_IN,
      user: null,
    }
  }

  componentDidMount(){
    if (this.props.token != null) {
      let config = {
        headers: {
          Authorization: `Bearer ${this.props.token}`,
        }
      }
      axios.get(window.location.origin + '/userData', config)
      .then(res=>{
        console.log(res.data);
        this.setState({
          user: res.data
        })
      })
      .catch(err=>{
        console.log(err);
      })
    }
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

  render(){
    switch(this.state.type) {
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
            <button onClick={this.onSigninClicked.bind(this)} class="auth-btn"><span class="auth-btn-text">Sign In</span></button>
        </div>
      )
      case this.Type.LOADING:
        return(
          <Loader 
            type="Circles"
            color="#00BFFF"
            height={60}
            width={60}
          />
        )
    }
  }
}

export default Auth;