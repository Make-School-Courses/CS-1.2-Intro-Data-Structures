## Class 10: Higher Order Markov Chains

### Activities
- Code review implementations of hash table class instance methods
- Lecture and discussion on building higher order Markov chains with larger window sizes

### Objectives
After completing this class session and the associated tutorial challenges, students will be able to ...
- Build higher order Markov chains based on observed frequency of *n*-grams (tuples of *n* words) in text
- Generate sentences by sampling words by performing random walks on higher order Markov chain
- Utilize a linked list as a queue to track words in a Markov chain's *n*-gram window

### Resources
- Read Victor Powell's [visual explanation of Markov chains] and play with the interactive animated diagrams
- Read Alex Dejeu's [article on how Markov chains work][Dejeu Markov article], with great examples specific to this project (only the "Intro To Markov Models" section; we'll cover the topics in the "Further Markov Model Topics" section later in the course)

### Challenges
These challenges are the baseline required to complete the project and course.
Be sure to complete these before next class session and before starting on the stretch challenges below.
- [Page 11: Markov Chains Revisited]
    - Build a second order Markov chain by analyzing frequency of adjacent words in text
    - Sample a random word from a state histogram in second order Markov chain
    - Generate a sentence by performing a random walk on second order Markov chain
- [Page 12: Creating a Corpus]
    - Choose a source with at least 20,000 words (ideally, well over 100,000 words)
    - Collect your corpus (use Diffbot corpus collection script if needed)

### Stretch Challenges
These challenges are more difficult and help you push your skills and understanding to the next level.
- [Page 11: Markov Chains Revisited]
    - Extend code used to build second order Markov chain to build *n*-th order Markov chain for varying values of *n* (from 1 up to ~5)
    - Implement `MarkovChain` class to store states of word frequency histograms
        - Add methods for constructing state histograms and sampling words
    - Handle beginning and end of sentences with special start and stop tokens
    - Use a linked list as a queue to track words in Markov chain's *n*-gram window
    - Implement circular buffer (fixed size queue)
    - Implement deque (double-ended queue)


[visual explanation of Markov chains]: http://setosa.io/blog/2014/07/26/markov-chains/
[Dejeu Markov article]: https://hackernoon.com/from-what-is-a-markov-model-to-here-is-how-markov-models-work-1ac5f4629b71
[Page 11: Markov Chains Revisited]: https://www.makeschool.com/academy/tutorial/tweet-generator-data-structures-probability-with-python/markov-chains-revisited
[Page 12: Creating a Corpus]: https://www.makeschool.com/academy/tutorial/tweet-generator-data-structures-probability-with-python/creating-a-corpus
