import praw
reddit = praw.Reddit(
    client_id="your client_id",
    client_secret="your client_secret",
    user_agent="some random string",
)
with open("top_jokes_year","w") as output_file:
    for submission in reddit.subreddit("jokes").top(limit=1000,time_filter="year"): # get top 1000 posts of all time from r/jokes
        output_file.write(submission.title) # write the title
        output_file.write("\n")             # write a new line character
        output_file.write(submission.selftext) # write the "body" of the post
        output_file.write("\n------------\n")# some dashes to separate one joke from another
