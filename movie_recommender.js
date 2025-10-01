


// 🎬 Movie Recommendation System
// Problem: People often waste time deciding what to watch. 
// Solution: Suggest movies based on the user's favorite genre.
// Concepts i used: Conditions, Loops, Functions

// Step 1: Store movies by genre
const movies = {
  action: ["Mad Max", "John Wick", "Avengers", "The Dark Knight"],
  comedy: ["The Mask", "Home Alone", "Jumanji", "Mr. Bean"],
  horror: ["The Conjuring", "IT", "Insidious", "A Quiet Place"],
  animation: ["Frozen", "Zootopia", "Toy Story", "Shrek"]
};

// Step 2: Function to display movies
function showMovies(genre) {
  if (movies[genre]) {
    console.log(`Here are some great ${genre} movies:`);
    // Loop through the movies in that genre
    for (let i = 0; i < movies[genre].length; i++) {
      console.log(`${i + 1}. ${movies[genre][i]}`);
    }
  } else {
    console.log("Sorry, we don’t have that genre. Try again!");
  } 
  let choice = prompt("Enter a movie genre (action, comedy, horror, animation) or type 'exit' to quit:");

  // Conditions to check the choice
  if (choice === "exit") {
    console.log("Thanks for using Movie Recommender! 🍿 Goodbye!");
    running = false; // stop the loop
  } else if (movies[choice]) {
    showMovies(choice); // call function to show movies
  } else {
    console.log("Invalid choice. Please try again!");
  }
}
