document.addEventListener("DOMContentLoaded", function () {
    const editPostForm = document.getElementById("editPostForm");
    const deletePostBtn = document.getElementById("deletePostBtn");

    editPostForm.addEventListener("submit", function (event) {
        const title = document.getElementById("title").value;
        const content = document.getElementById("content").value;

        if (!title || !content) {
            event.preventDefault();
            alert("Please fill out all fields.");
        }

        // Set form action based on whether it's an edit or add operation
        const postId = document.getElementById("postId").value;
        const formAction = `/edit_post/${postId}/` + (postId ? '' : 'add_edit_post/');
        editPostForm.setAttribute("action", formAction);
    });

    deletePostBtn.addEventListener("click", function () {
        const confirmDelete = confirm("Are you sure you want to delete this post?");
        if (confirmDelete) {
            // Perform the delete action
            const postId = document.getElementById("postId").value;
            alert(`Deleting post with ID: ${postId}`);
            // Add logic to redirect or handle delete on the same page
        }
    });
});
