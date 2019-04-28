// import React from 'react';
//
// class LoadingBar extends React.Component {
//   constructor(props) {
//     super(props);
//     this.enableMessage = this.enableMessage.bind(this);
//
//     this.state = {
//       displayMessage: false,
//     };
//
//     this.timer = setTimeout(this.enableMessage, 250);
//   }
//
//   componentWillUnmount() {
//     clearTimeout(this.timer);
//   }
//
//   enableMessage() {
//     this.setState({displayMessage: true});
//   }
//
//   render() {
//     const {isBusy} = this.props;
//
//     if (isBusy) {
//       return <LoadingBar/>;
//     }
//
//     return <div>Ready!</div>;
// };
//
// export default LoadingBar;
