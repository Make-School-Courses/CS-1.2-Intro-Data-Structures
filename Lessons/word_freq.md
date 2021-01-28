# Frequency Counting with a Hash Table 📊


## Description

One standard use of a hash table is counting the frequency of words in a file. For this assignment, you will use a hash table to implement a word-frequency counting program. 


## Setup

🚨 Before starting the assignment, watch [How to: Setup for a New Assignment](https://youtu.be/MCbDO8IpqZM).

This tutorial walks you through how to set up a new repository, make commits, and push code to Github.



## Requirements

### Submission Requirements:
1. Your submitted code should be in a new (public) repo on Github.
1. Your repository should have a minimum of **5 commits**. 
1. Your repo should include a README with the name of your project and a description.
1. Create a demo video. The demo should include a walkthrough of your code and demonstration of your project working.
1. [Optional] Upload your video to Google Drive and share a link if Gradescope upload speeds are too slow.
1. Submit the link to your repo and demo on [Gradescope](https://www.gradescope.com/courses/202248/assignments/803584).

### Assignment Requirements:

Your program will do the following:
* Count the number of occurrences of each word in the file.
* Print all of the words and their frequencies. 

For example, a text file that contains these lines:

```
I write, erase, rewrite
Erase again, and then
A poppy blooms.
```

would generate this output:
```
a: 1
again: 1
and: 1
blooms: 1
erase: 2
i: 1
poppy: 1
rewrite: 1
then: 1
write: 1
```

Assumptions:
* Words will be counted in a case-insensitive manner (For example, in the above example, `Erase` and `erase` are counted as the same word.)
* Punctuation is ignored. You can use a delimiter to ignore the following characters: `, . ; : - ? !`
* Assume that the input file consists of letter-only words (That is, the file will not have words that contain apostrophes such as `isn’t` and `‘tis`).




### Stretch Challenges (Optional)
1. Print the total number of distinct words at the beginning of your program.
1. Offer the user a prompt to query the exact count of a particular word.
1. Offer the user a prompt to delete a word that exists in your Hash Table. 



## Rubric

Coming soon.
