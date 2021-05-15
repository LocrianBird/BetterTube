import React, {useState} from 'react';
import '../ComponentStyle/videoGridStyle.css';
import axios from 'axios';
import RefreshBtn from '../ComponentStyle/img/refresh.png';
import Loader from 'react-loader-spinner';

const VideoCard = (props) => {
  return(
    <div className="video-card-div">
      <a href={props.link} className="video-card">
        <div className="video-card-thumbnail">
          <img src={props.thumbnail}/>
          <div className="video-card-timebox">
            <p>{props.time}</p>
          </div>
        </div>
        <div className="video-card-info">
          <p className="video-card-caption">{props.caption}</p>
          <div className="video-card-subinfo">
            <p className="video-card-timeposted">{props.timeposted}</p>
            <p className="video-card-creator">{props.creator}</p>
          </div>
        </div>
      </a>
    </div>
  )
}

class VideoGrid extends React.Component {
  constructor(props){
    super(props);
    this.state = {
      videoGridState: []
    }
    //this.props = props;
  };


  componentDidMount() {
    let config = {
      headers: {
        Authorization: `Bearer ${this.props.token}`,
      }
    }
    axios.get(window.location.origin + '/home', config)
    .then(res=>{
      this.setState({
        videoGridState: res.data
      })
    })
    .catch(err=>{
      console.log(err);
    })
  }

  render(){
    return(
      <div className="home">
        { this.state.videoGridState.length > 0 &&
          <div className="video-grid-info video-grid-new" id="video-grid-new">
            <button className="video-grid-refresh-btn">
              <img src={RefreshBtn} className="video-grid-refresh" width="40px" height="40px"/>
            </button>
            <p className="video-grid-text new">New</p>
          </div>
        }
        { this.state.videoGridState.length === 0 ? 
          <div className="onload-spinner">
            <Loader 
              type="Puff"
              color="#e2a917"
              height={50}
              width={50} />
            </div> :
          <div className="video-grid">
            {this.state.videoGridState.map((video) => {
              return <VideoCard 
                      thumbnail={video.thumbnail} 
                      caption={video.caption} 
                      link={video.link} 
                      time={video.time}
                      timeposted={video.timeposted}
                      creator={video.creator}/>
            })}
          </div>
        }
      </div>
    )
  }
}

export default VideoGrid;