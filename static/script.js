function confirmDelete(postId) {
    if (confirm("이 통신 기록을 삭제하시겠습니까?")) {
        
        location.href = "/delete/" + postId;
    }
}
