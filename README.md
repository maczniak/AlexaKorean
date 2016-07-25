# AlexaKorean

Alexa (Amazon Echo) supports English voice input and output only now. But you
can provide a phonemic pronunciation or play mp3 clips by using [Speech
Synthesis Markup Language][ssml] (SSML). Although SSML supports a limited set
of symbols, this script mimics Korean speech as close as possible.

## Usage

```python
output1 = AlexaKorean.speak("BBQ양념치킨")
// <say-as interpret-as="characters">BBQ</say-as><phoneme alphabet="ipa" ph="jɑŋ.njʌm.t͡ʃi.kin.">양념치킨</phoneme>
output2 = AlexaKorean.speak("그래 오늘은 안녕", AlexaKorean.IPA) // default: IPA
// <phoneme alphabet="ipa" ph="g.ɹɛ.">그래</phoneme> <phoneme alphabet="ipa" ph="oʊ.nl.n.">오늘은</phoneme> ...
output3 = AlexaKorean.speak("hello world 예제", AlexaKorean.SAMPA)
// hello world <phoneme alphabet="x-sampa" ph="jE.dZE.">예제</phoneme>
```

You can hear outputs at Test > Voice Simulator in [developer
console][developer_console].

## Known Issue

* affected 'ㅗ' (h**o**g) and 'ㅜ' (f**oo**t) sounds

## TODO

* complete a phonemic mapping table
* support ordinal numbers
* support symbols
* support phonological rules ([wikipedia][korean_phonology],
  [reference][standard])
* use '을' or '를' properly
* tell short vowels from long vowels
* testcases
* JavaScript version
* package, deployable to AWS Lambda
* sample output

[ssml]: https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/speech-synthesis-markup-language-ssml-reference
[developer_console]: https://developer.amazon.com/edw/home.html#/skills
[unicode_jamo]: https://en.wikipedia.org/wiki/Hangul_Jamo_(Unicode_block)
[korean_phonology]: https://en.wikipedia.org/wiki/Korean_phonology
[standard]: http://www.korean.go.kr/front/page/pageView.do?page_id=P000085

