document.getElementById('postForm').addEventListener('submit', postMessage);

function postMessage(event) {
  event.preventDefault();
  
  var username = document.getElementById('username').value;
  var content = document.getElementById('postContent').value;
  
  // Create post element
  var post = document.createElement('div');
  post.classList.add('post');
  
  var usernameElement = document.createElement('div');
  usernameElement.classList.add('username');
  usernameElement.textContent = username;
  
  var contentElement = document.createElement('div');
  contentElement.classList.add('content');
  contentElement.textContent = content;
  
  // Append post elements to the discussion container
  post.appendChild(usernameElement);
  post.appendChild(contentElement);
  document.getElementById('threadedDiscussions').appendChild(post);
  
  // Clear form fields
  document.getElementById('username').value = '';
  document.getElementById('postContent').value = '';
}