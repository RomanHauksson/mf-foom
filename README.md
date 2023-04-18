# MF FOOM

I fine-tuned GPT-3 on the lyrics of 96 MF DOOM songs to write rap lyrics in his style. Then, I used ElevenLabs to clone his voice and make him rap the lyrics.

## Demo

https://user-images.githubusercontent.com/62364808/232918506-4b40215b-728b-4879-9631-8c5107e28855.mp4

### Input prompt

> A song titled "Metal Mask" about the story of how MF DOOM obtained his iconic metal mask and the power it gives him in the rap game.

### Output lyrics

> Metal Mask Lyrics[Verse: MF DOOM + Samples]
Metal mask give him bad brains, pain man can't explain\
Got locked up like a zoo monkey, then poof! Freedom\
Got loose, left the cell, started rockin fools clean\
Like a hill of beans, beans, no pan dulce\
The rap game is like the seventh seal, it's so real\
He hide behind a mask like a child, it's cold steel\
No regrets, he do what he gotta and he peep this\
I hold this, zap! Straight out the box, no joke\
Deadly as a runaway stampede or lightning bolt in Summertime\
Big as a Bumblebee sting and quicker to bring strife\
Through the big speakers, sound bombs, ignite drama\
On my A-game, I be straight sniper, through your eye likeGrey's Anatomy\
White chick that be in the show with all them doctors\
Know what I'm saying? The name control the ball like gridiron\
Speech, diction, syntax is triple A rated\
And it's not how he talk it, who he talk to\
To all y'all that hate, keep your mouth closed\
(DOOM!) Watch the mask and you'll see\
And say your prayers, like "Boom! He's back!"\
You won't see me, I disappear like Dr. Jekyll and Mr. Hyde\
Boogie blow, snatch the dough then split like Houdini\
Like a palm tree in Africa, can't stand still\
With the metal mask, give him mad-r'dic skills\
Like Kung Fu, uncanny too and always get it poppin'\
Always gone, always goon, on the road that's how it seem\
Seriously, he be writing on the tour like Forrest Gump\
Went to dinner with the 'mentor', it was crazy dude\
He gave him advice, he told him what life was about\
We got beef with Jim Crow and don't forget\
The name is DOOM, the mask gives him powers

## Technical details

- `lyrics.py` downloads the lyrics of every MF DOOM song from Genius.com and saves them to lyrics.json.
- `prompts.py` generates a one-sentence summary of each song and uses each summary–lyrics pair to generate fine-tuning prompts, which it saves in `prompts.jsonl`.
- I cleaned up the prompts by removing any string in `prompts.jsonl` which matched the regular expressions `You might also like.{0,3}Embed`, `You might also like`, or `\d*Embed`.
- Then, I ran `openai api fine_tunes.create -t prompts.jsonl -m davinci` in the terminal to fine-tune a GPT-3 Davinci model on the prompts and then generated an example in the OpenAI API Playground.
    - I used default generation settings, except a temperature of 0.9 and a presence penalty of 0.46.
- I used [ElevenLabs](https://beta.elevenlabs.io/) to clone DOOM's voice from [the acapella version of *Gazzillion Ear*](https://www.youtube.com/watch?v=LoXJd4Hkbcg).
    - I then generated the vocals from the lyrics using this clone with a stability of 86% and a similarity of 100%.
- Finally, I overlaid the vocals onto [the instrumental of *Gazzillion Ear*](https://www.youtube.com/watch?v=sQ7aKsYxwaM).

*The lyrics I generated and the final song Metal Mask are a non-commercial parody.*
