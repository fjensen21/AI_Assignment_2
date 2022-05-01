THIS README IS MANLY TO EXPLAIN INPUT / OUTPUT FOR PARTS B AND C.

ALL I/O will be written to and read from the files in directory Ground_Truth.
The naming of said files would be in the form of "test{}.txt" where {} is the number of the test file.
When running part_B.py you get to choose how many files to create.

The I/O Format is the following:
- First two lines for number of rows and columns respectively.
- Next two lines for initial position (X_initial, Y_initial respectively).
- Next 100 lines is a list of Actions to be attempted.
- Next 100 lines is the actual location of the agent after attempting the respective action.
- Next 100 lines is the observation of the agent after attempting the respective action.
