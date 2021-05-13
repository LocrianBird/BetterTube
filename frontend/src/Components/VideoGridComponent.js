import React, {useState} from 'react';
import '../ComponentStyle/videoGridStyle.css';
import axios from 'axios';


const VideoCard = (props) => {
  return(
    <div className="video-card">
      <a href={props.link}>
        <img src={props.thumbnail}/>
        <p>{props.caption}</p> 
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
  };


  componentWillMount() {
    axios.get(window.location.origin + '/recommendations')
    .then(res=>{
      console.log(res.data);
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
      <div className="VideoGrid">
        {this.state.videoGridState.map((video) => {
          return <VideoCard thumbnail={video.thumbnail} caption={video.caption} link={video.link}/>
        })}
      </div>
    )
  }
}

export default VideoGrid;