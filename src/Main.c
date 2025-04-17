#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
bool searchWord(char** board, int boardSize, int* boardColSize, char* word, bool** visited, int h, int i, int j);
bool exist(char** board, int boardSize, int* boardColSize, char* word) { 
    if( board == NULL || boardSize == 0 || word == NULL || word[0] == '\0' ){
        return false;
    }

    bool **visited = (bool**)malloc(boardSize * sizeof(bool*)); //number of bytes to allocate
    for(int i = 0 ; i < boardSize ; i++){
        visited[i]=(bool*)calloc(boardColSize[i], sizeof(bool)); //number of blocks to allocate and size of each
    }

    bool found = false;
    for (int i = 0; i<boardSize; i++){
        for (int j=0 ; j<boardColSize[i]; j++){
            if( word[0] == board[i][j] ){
                visited[i][j] = true;
                if((word[1] == '\0') || searchWord(board, boardSize, boardColSize, word, visited, 1, i, j)){
                    found = true;
                    break;
                }
                visited[i][j] = false; //backtrack
               
            }
        }
    }

    for(int i = 0 ; i < boardSize ; i++){
        free(visited[i]); //freeing the memory allocated for each row
    }
    free(visited); //freeing the memory allocated for the array of pointers
    return found; //returning the result

}

bool searchWord(char** board, int boardSize, int* boardColSize, char* word, bool** visited, int h, int i, int j){
    if(word[h] == '\0'){
        return true;
    }
    else{
        if ((i+1 < boardSize) && board[i+1][j] == word[h] && visited[i+1][j] == false){
            visited[i+1][j] = true;
            if(searchWord(board, boardSize, boardColSize, word, visited, h+1, i+1, j)){
                return true;
            }
            visited[i+1][j] = false; //backtrack

        }
        if ((i-1 >= 0) && board[i-1][j] == word[h] && visited[i-1][j] == false){
            visited[i-1][j] = true;
            if(searchWord(board, boardSize, boardColSize, word, visited, h+1, i-1, j)){
                return true;
            }
            visited[i-1][j] = false; //backtrack

        }
        if ((j+1 < boardColSize[i]) && board[i][j+1] == word[h] && visited[i][j+1] == false){
            visited[i][j+1] = true;
            if(searchWord(board, boardSize, boardColSize, word, visited, h+1, i, j+1)){
                return true;
            }
            visited[i][j+1] = false; //backtrack

        }
        if ((j-1 >= 0) && board[i][j-1] == word[h] && visited[i][j-1] == false){
            visited[i][j-1] = true;
            if(searchWord(board, boardSize, boardColSize, word, visited, h+1, i, j-1)){
                return true;
            }
            visited[i][j-1] = false; //backtrack

        }
        return false; //if all directions are exhausted and no match is found

    }

}