

function create_piece(square_num)
{
    // Select the target container by ID
    const boardSingle = document.getElementById('board-single');
    
    // Check if the container exists
    if (boardSingle) {
        // Create a new div element
        const pieceDiv = document.createElement('div');

        // Add the desired classes to the new div
        pieceDiv.className = 'piece square-' + square_num;

        // Add inline styles (if any)
        pieceDiv.style.cssText = ''; // No styles provided, this is an empty style

        // Append the new div to the target container
        boardSingle.appendChild(pieceDiv);

        console.log('Piece created and added to #board-single:', pieceDiv);
    } else {
        console.error('Element with ID "board-single" not found.');
    }

}


create_piece('84')
for (let i = 1; i <= 8; i++) {
    for (let j = 1; j <= 8; j++) {
        create_piece(i + '' + j)
    }
}
