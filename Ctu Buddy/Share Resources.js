document.getElementById('uploadForm').addEventListener('submit', uploadResource);
document.getElementById('searchInput').addEventListener('input', searchResources);

function uploadResource(event) {
  event.preventDefault();
  
  var resourceName = document.getElementById('resourceName').value;
  var resourceFile = document.getElementById('resourceFile').files[0];
  var resourceCategory = document.getElementById('resourceCategory').value;
  var resourceTags = document.getElementById('resourceTags').value.split(',');
  
  // Create resource item
  var resourceItem = document.createElement('li');
  resourceItem.innerHTML =
    '<h3>' + resourceName + '</h3>' +
    '<p>Category: ' + resourceCategory + '</p>' +
    '<p>Tags: ' + resourceTags.join(', ') + '</p>' +
    '<a href="' + URL.createObjectURL(resourceFile) + '" download>Download</a>';
  
  // Append resource item to the list
  document.getElementById('resourceItems').appendChild(resourceItem);
  
  // Clear form fields
  document.getElementById('resourceName').value = '';
  document.getElementById('resourceFile').value = '';
  document.getElementById('resourceCategory').value = '';
  document.getElementById('resourceTags').value = '';
}

function searchResources() {
  var searchQuery = document.getElementById('searchInput').value.toLowerCase();
  var resourceItems = document.getElementById('resourceItems').children;
  
  var showCount = 0;
  
  for (var i = 0; i < resourceItems.length; i++) {
    var resourceItem = resourceItems[i];
    var resourceText = resourceItem.innerText.toLowerCase();
    
    if (resourceText.includes(searchQuery)) {
      resourceItem.style.display = 'block';
      showCount++;
    } else {
      resourceItem.style.display = 'none';
    }
  }
  
  var noResultsMsg = document.getElementById('noResultsMsg');
  if (showCount === 0) {
    noResultsMsg.innerHTML = 'No results found.';
  } else {
    noResultsMsg.innerHTML = '';
  }
}