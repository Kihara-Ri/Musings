# About English

I just finished my TOEFL voabulary on a whim, with the total words of 4882 and I spent 7429 min in total to complete that. The TOEFL vocabulary feels very formal to me, and it's hard to use these words in everyday life, and moreover I am a perfectionist by nature, so not being familiar with these words makes it difficult for me to use them in conversation, which makes me very frustrated. TOEFL needs you to be a fluent speaker and think of things like a native speaker. During the test, you are only given several seconds to organize your answer, and you talk, without pausing. Which is really difficult for me as I cannot even make it in my mother tongue. I'm the kind of person who always try to compose a sentence with formal vocabulary, so sometimes when I cannot come up with the correct word I'm going to say, I usually stand still speaking nothing. So I wonder if there really exists people like Seldon in *The Big Bang Theory*?

Therefore, I will soon start studying for the IELTS to be able to express myself in authentic English. From now, I'm gonna record some native or natural expressions:

- **Planet of Solar System** in order from nearest to farthest: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune.
- **Summer Triangle** known as the 夏の大三角形: Altair(アルタイル), Deneb(デネブ) and Vega(ベガ)
- **bosom**: The bosom, a small waist, and generous hips, and this was the prized look of the victorian time (and so does now). She cradles me in her bosom.
- **benign**: If you want to say that a person is good and don't do bad things, do not simply say good or kind, just say a benign person. And you can also use like this: a benign smile, a benign weather. And perhaps she was able to detect benign people from dangerous people.
- **balm**: This word is not usually used by male cause we hardly use these things. One sentence to remember this word: When I feel my lips are dry and cracked, I would wear lip balm.
- **myopic**: The rate of myopia in Chinese primary and secondary schools is very high.
- **salon**: When you gotta get your hair cut, you'd go to the hair salon.
- **thaw**: Temperatures have been rising for years, causing the ice to thaw. Thaw is mainly used to describe the process of something frozen becoming soft or liquid as a result in temperature, related to weather or cooking. Melt can be used more broadly like butter, chocolate or metal.
- **far-fetched**: It does sound a bit far-fetched. You can use this word as a substitute for unbelievable. 
- **antagonist**: Synonyms of opponent, rival, competitor.
- **quench**: Once they've quenched their thirst, the next priority is food. Quench your thirst.
- **executive**: CEO(Chief Executive Officer), CFO(Chief Financial Officer), COO(Chief Operating Officer). Senior executive, executive car.
- **instructor**: Someone who teacher or educates others, typically in s specific subject or skill. And the lowest level teacher in university is called instructor. A driving instructor.
- **converse**: When you talk to someone, you better use converse with someone.
- **perceive**: The face is a large part of how people perceive you during interactions. If you want to say how you think of someone or something, you can use perceive. She perceived a faint smell of coffee in the air. He perceived that she was unhappy, even though she didn't say anything(空気読み). Voters perceive him as a strong leader, although his policies have been controversial.
- **conceive**: I cannot conceive of a life without you.
- **diction**: Diction is the biggest problem of my English. It typically considers: level of formality, precision and clarity, tone and atmosphere, characterization
- **glaze**: He explains his ideas in agonizing detail until everyone's eyes glaze over.

One finding of English. We often mock the Japanese people pronounce English. For example *swing*, Japanese pronounce スウィング with g pronounced with グ. Well that sounds a little ridiculous for us Chinese becuause we assume that the `g` here is silent. The fact is that when American people pronounce the single word swing, they pronounce the `g`. 

What's the difference between checked shirts and plaid shirts?

> Plaids and checks. These two words often show up together, but they are not actually interchangeable. They refer to different types of patterns. Before we get into the differences between a plaid and a check, it's important to know that both words traditionally describe a woven cloth. Plaids and checks are both designs historically made as woven cloth. And to understand woven cloth patterns, you need to know the basics about weaving. Weaving is a preocess of creating fabric by interlacing two yarn systems, the warp and the weft. The warp yarns run lengthwise through a fabric and are wound onto a loom and held under tension. The weft yarns are pu in one at a time by a weaver, crosswise through the fabric. The two yarn systems interlace at right angles to each other. The weaving process is the same, whether done by a person sitting at a loom or by a mechanized loom. Many fabrics are woven on a solid color warp, but plaids and checks are both made on a warp with a stripe pattern. The strip pattern for the warp contains varying different color threads and different size stripes. In plaids and checks, the stripe patern is not random across the warp's width but has a regular, repeating pattern. Likewise, the weft yarns are also in a stripe pattern of different colors and sizes. The difference between plaids and checks lies in these repeating patterns. Checks are two colors and have the same stripe pattern in the warp and the weft. The finished cloth is always symmetrical. Plaids have more than two colors and more variety in their stripe layouts.

So, to conclusion, the stereotype of shirts weared by programmers is actually plaids.



# About data wrangling

I just suddenly came out of some functions implemented by command line.

## find

I want to find files that end with `.mkv` and calculate the sum of disk space they occupies:

```bash
find . -type f -name "*.mkv" -exec du -ch {} + | grep total$
```

This command is quite complicated, let's analyise the parts:

- `exec du -ch {} +`, for every found file, execute command `du`, short for "disk usage", `-ch` means "cumulative" and "human-readable", "cumulative" tells `du` to output the total size of all specified files after processing. `{}` is a placeholder. The `find` command replaces this with the path of each found file. `+` ends the list of parameters for the `-exec` command and tells the `find` to pass all found files to the `du` at once, rather than invoking `du` for each file found. This improves efficiency since `du` is launched only once, not multiple times.
- And then we pass the calculated size to command `grep` with a pipe. The `grep` do `grep total$`, which means you just want to see the total size, rahter than sizes of other single files, so this is a filter. `total$` is just a special symbol in regular expressions representing the end of a line. So this means I just want the on line that ends up with `total`.

This command is a little bit abstract to understand, let's make a simple experiment.

First, I `touch` 10 files that end with `.mkv`, and `find . -type f -name "*.mkv"` to find them:
```bash
$ touch {1..10}.mkv

$ find . -type f -name "*.mkv"

./1.mkv
./9.mkv
./7.mkv
./8.mkv
./6.mkv
./2.mkv
./3.mkv
./5.mkv
./10.mkv
./4.mkv
```

The I calculate their size:

```bash
$ find . -type f -name "*.mkv" -exec du -ch {} +

0       ./1.mkv
0       ./9.mkv
0       ./7.mkv
0       ./8.mkv
0       ./6.mkv
0       ./2.mkv
0       ./3.mkv
0       ./5.mkv
0       ./10.mkv
0       ./4.mkv
0       total

```

With a filter:

```bash
$ find . -type f -name "*.mkv" -exec du -ch {} + | grep total$
0       total # highlighted
```

And you can see that `total` is highlighted.

## clipboard

If you want to copy your output of your command, you can use `xclip`. Seems you gotta intall it with apt:

```bash
sudo apt install xclip
```
Using:

```bash
your-command | xclip -selection clipboard
```

And you will get the output in your clipboard, which is quite convenient when you want to use this as one more input.

You can also use `$(!!)` to execute your last command again:

```bash
echo "$(!!)" | xclip -selection clipboard
```

## grep

`grep` is a very powerful tool for text search. If you want to searh files that contains "English", and you just need to know the file name, you can use this command:

```bash
grep -l "English" *
```

Recursively in current directory:

```bash
grep -r -l "English" .
```

Ignore case (uppercase and lowercase of letter) with `-i`

```bash
grep -r -l -i "englisha" .
```

Find some files of specialized form, using `--include`:

```bash
grep -r -l -i --include="*.md" "english" .
```

