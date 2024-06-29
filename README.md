# Paper Summary Bot
<hr>

## 개요
MS Teams에서 유저와 봇의 상호작용만으로 요약된 논문을 빠르게 읽을 수 있는 봇 개발

## 목적
URL(저장위치) 입력만으로 원하는 논문을 빠르게 요약해 업무 효율성을 향상 시키기 위한 목적으로 개발함

## 프로젝트 기간 
2023.11.21 ~ 2022.12.22

## 사용기술
- Language : Python 3.8 <br>
- Bot : MS Bot Framework SDK<br>
- API : OpenAI API<br>
- Network Tunneling : Ngrok

## 기능설명
- 유저는 논문 URL 또는 논문 저장위치를 봇에 입력
- 봇은 langchain 모듈을 통해 논문 내용을 파싱
- 파싱된 논문(text), 논문요약 프롬프트, 파라미터를 openai_api를 통해 설정된 모델(ex gpt-4-1106-preview)에 전달
- 모델의 요약 결과를 유저에게 전달

## 요약결과

![inital](https://github.com/Kingthegarden/paper_summary_bot/assets/63918254/424a170d-20eb-42d2-b42b-3f2c7467e213)
