document.addEventListener("DOMContentLoaded", function () {
    const addPostForm = document.getElementById("addPostForm");
    const deletePostForm = document.getElementById("deletePostForm");

    addPostForm.addEventListener("submit", function (event) {
        // Add form validation logic here
        const title = document.getElementById("title").value;
        const content = document.getElementById("content").value;

        if (!title || !content) {
            event.preventDefault();
            alert("Please fill out all fields.");
        }
    });

    deletePostForm.addEventListener("submit", function (event) {
        // Add form validation logic here
        const postId = document.getElementById("postId").value;

        if (!postId || isNaN(postId)) {
            event.preventDefault();
            alert("Please enter a valid Post ID.");
        }
    });
});
