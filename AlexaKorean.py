#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals
from functools import partial

def concat(dlst): # flatten
	return [x for lst in dlst for x in lst]

def partition(fun, col):
	if not col:
		return []
	ret = []
	it = iter(col)
	
	x = next(it)
	acc = [x]
	last = fun(x)

	for x in it:
		curr = fun(x)
		if curr == last:
			acc.append(x)
		else:
			ret.append(acc)
			acc = [x]
		last = curr
	ret.append(acc)
	return ret

class AlexaKorean:

	initials = [
		# ㄱ ㄲ ㄴ ㄷ ㄸ
		("giyeok","g","g"), ("ssanggiyeok","gˈ","g\""), ("nieun","n","n"), ("digeut","d","d"), ("ssangdigeut","dˈ","d\""),
		# ㄹ ㅁ ㅂ ㅃ ㅅ
		("rieul","ɹ","r\\"), ("mieum","m","m"), ("bieup","b","b"), ("ssangbieup","pˈ","p\""), ("siot","s","s"),
		# ㅆ ㅇ ㅈ ㅉ ㅊ
		("ssangsiot","sˈ","s\""), ("ieung","",""), ("jieut","d͡ʒ","dZ"), ("ssangjieut","d͡ʒˈ","dZ\""), ("chieut","t͡ʃ","tS"),
		#ㅋ ㅌ ㅍ ㅎ
		("kieuk","k","k"), ("tieut","t","t"), ("pieup","p","p"), ("hieut","h","h")
	]
	
	medials = [
		# ㅏ ㅐ ㅑ ㅒ ㅓ
		("a","ɑ","A"), ("ae","ɛ","E"), ("ya","jɑ","jA"), ("yae","jɛ","jE"), ("eo","ʌ","V"),
		# ㅔ ㅕ ㅖ ㅗ ㅘ
		("e","ɛ","E"), ("yeo","jʌ","jV"), ("ye","jɛ","jE"), ("o","oʊ","oU"), ("wa","wɑ","wA"),
		# ㅙ ㅚ ㅛ ㅜ ㅝ
		("wae","wɛ","wE"), ("oe","ə","@"), ("yo","joʊ","joU"), ("u","ʊ","U"), ("wo","wɚ", "w@`"),
		# ㅞ ㅟ ㅠ ㅡ ㅢ
		("we","wɛ","wE"), ("wi","wi","wi"), ("yu","ju","jU"), ("eu","",""), ("ui","ʊ","U"),
		#ㅣ
		("i","i","i")
	]
	# ("ae","æ","{"), ("eu","ʊ","U"), ("i","ɪ","I")
	
	finals = [
		# none ㄱ ㄲ ㄳ ㄴ
		("none","",""), ("giyeok","g","g"), ("ssanggiyeok","k","k"), ("giyeok-siot","g","g"), ("nieun","n","n"),
		# ㄵ ㄶ ㄷ ㄹ ㄺ
		("nieun-jieut","nd͡ʒ","ndZ"), ("nieun-hieut","n","n"), ("digeut","d","d"), ("rieul","l","l"), ("rieul-giyeok","k","k"),
		# ㄻ ㄼ ㄽ ㄾ ㄿ
		("rieul-mieum","m","m"), ("rieul-bieup","l","l"), ("rieul-siot","l","l"), "rieul-tieut", "rieul-pieup",
		# ㅀ ㅁ ㅂ ㅄ ㅅ
		"rieul-hieut", ("mieum","m","m"), ("bieup","b","b"), ("bieup-siot","b","b"), "siot",
	# ㅆ ㅇ ㅈ ㅊ ㅋ
	("ssangsiot","d","d"), ("ieung","ŋ","N"), "jieut", "chieut", "kieuk",
	# ㅌ ㅍ ㅎ
	("tieut","t","t"), ("pieup","p","p"), ("hieut","d","d")
	]
	
	IPA = 1
	XSAMPA = 2

	@staticmethod
	def notation_name(notation):
		if notation == AlexaKorean.IPA:
			return "ipa"
		if notation == AlexaKorean.XSAMPA:
			return "x-sampa"
		return ""

	@staticmethod
	def is_korean(c):
		return c >= "가" and c <= "힣"
	@staticmethod
	def is_upper(c):
		return c >= 'A' and c <= 'Z'

	@staticmethod
	def parse_characters_by_type(s):
		par = partition(AlexaKorean.is_korean, s)
		par = concat([partition(AlexaKorean.is_upper, a) for a in par])
		return ["".join(x) for x in par]

	@staticmethod
	def parse_korean_character_by_jamo(ch):
		c = ord(ch)
		c -= 44032
		final = c % 28
		c /= 28
		medial = c % 21
		c /= 21
		initial = c
		return (initial, medial, final)
	
	@staticmethod
	def phonological_transform(syls):
		return syls

	@staticmethod
	def read_syllables(syls, notation):
		if not (notation == AlexaKorean.IPA or notation == AlexaKorean.XSAMPA):
			return []
		return "".join([AlexaKorean.read_syllable(syl, notation)
						for syl in syls])

	@staticmethod
	def read_syllable(syl, notation):
		return "%s%s%s." % (AlexaKorean.initials[syl[0]][notation],
		                    AlexaKorean.medials[syl[1]][notation],
		                    AlexaKorean.finals[syl[2]][notation])
	
	@staticmethod
	def speak(s, notation = IPA):
		ret = []
		splitted = AlexaKorean.parse_characters_by_type(s)
		return "".join(map(partial(AlexaKorean._speak, notation = notation),
							splitted))

	@staticmethod
	def _speak(seg, notation):
		if AlexaKorean.is_korean(seg):
			lst = [AlexaKorean.parse_korean_character_by_jamo(x) for x in seg]
			ph = AlexaKorean.read_syllables(
						AlexaKorean.phonological_transform(lst),
						notation)
			return '<phoneme alphabet="%s" ph="%s">%s</phoneme>' % \
						(AlexaKorean.notation_name(notation), ph, seg)
		elif AlexaKorean.is_upper(seg) and len(seg) > 1:
			return '<say-as interpret-as="characters">%s</say-as>' % seg
		else:
			return seg

#print(AlexaKorean.speak("짜장면"))

