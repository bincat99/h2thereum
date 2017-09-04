# Bitcoin docs for newbie
---

## index
1. Understand Bitcoin
1.1 What is Bitcoin?
1.2 What is mining?
1.3 What is process of Bitcoin transaction? (to be added)

## 1. Understand Bitcoin
### 1.1 What is Bitcoin?
비트코인이 무엇인지 처음 알아보려 할 때 흔히 보이는 키워드가 몇 가지 있다. 블록체인, 채굴, 논스(nonce), 가상화폐 등 난해한 단어들이 등장하는데 이를 이해하기 위해서는 피똥싸면서 문서를 읽어야 가능하기 때문에 굉장히 불편하다.

가장 먼저 이해해야할 사실은 다음과 같다
* `Bitcoin != Block Chain`
* `Bitcoin != Block`

첨언을 하자면 `Bitcoin`은 흔히 거래소 혹은 지갑에서 BTC 단위로 표현되는 화폐이다. 이 녀석이 진짜 가상화폐이며 정말 실체가 존재하지 않는다. `Bitcoin`의 소유권은 오직 장부에 있는 기록으로만 증명할 수 있다. 이 장부가 바로 `Block Chain`이며 이를 구성하는 각 `Block`은 거래 내용들을 기록한 페이지가 된다.

따라서 어떤 사람 A가 얼마의 비트코인을 소유하고 있는지 확인하기 위해서는 장부를 첫 페이지부터 차례대로 읽어가며 확인하는 방법 뿐이다. 각 페이지에서 A가 연관된 거래 내역만 꺼내어 계산한다. 그러면 장부를 모두 읽고난 후에 계산된 결과가 A가 현재 소유하는 비트코인의 양을 가리킬 것이다.

### 1.2 What is mining?
비트코인에 대한 이야기를 할 때 흔히 나오는 '비트코인을 채굴한다'라는 표현이 있다. `mining`은 비트코인 화폐를 발행하는 방식을 일컫는 말이다. 정확히 말하면 비트코인은 채굴에 대한 보상이고, 채굴한다는 행위가 무엇인지 알아야 채굴 대상도 이해하기 쉽다.

비유하자면 채굴은 장부의 페이지를 만들어 나가는 행위이고 실제로는 `Block`을 생성하는 과정이다. 채굴 과정에 참여하는 사람은 '어떤' 값을 찾아야 한다. 다음 예시를 보자.
```
sha256 ("H2thereum" + "779312") => 0x000ee07b294194bb51231ba7a1bbd89d157c18981c1eb488f22b94d0513d348c
sha256 ("H2thereum" + "779858") => 0x00000fdb6c96ae4d9b94c688940989e82f12824bda249f7dc1f7671e25cdd34b
sha256 ("H2thereum" + "788805") => 0x0007c9e29e1090ffd27fe929a026a1d301c7cee4e875764cf1731de73e12a4d5
```

sha-256 hash 값의 앞 부분이 0으로 시작한다. 이처럼 특정한 데이터 ("H2thereum")에 추가된 '어떤' 값을 `nonce`라 하며, `sha256(data + nonce)` 값의 앞 부분이 몇 개의 0으로 시작하게 되는 nonce 를 찾는 것이 마이닝에 참여한 사람들의 목표다. 종종 이를 '수학 문제를 푼다'고 표현하는데, 이 때 말하는 문제가 [hash cash] 이다. 

특정한 데이터는 다음과 같이 정의 된다.
* `data = 이전 블록의 hash 값 + 현재 블록에 저장될 Transactions`

이전 블록은 현재 시점의 블록 체인에서 가장 마지막 블록을 말한다. 그리고 위의 문제를 푸는 nonce 값을 찾으면 새로운 블록이 생기고 블록 체인에 추가되는 것이다.


## TO DO LIST


## Reference

* [ethereum White-paper](https://github.com/ethereum/wiki/wiki/White-Paper)
* [비트코인과 블록체인 기술](http://d2.naver.com/helloworld/8237898)
* [블록체인 선행지식](https://medium.com/@soonhyungjung/%EB%B8%94%EB%A1%9D%EC%B2%B4%EC%9D%B8-%EA%B3%B5%EB%B6%80-%EC%9E%90%EB%A3%8C-%EC%A0%95%EB%A6%AC%EC%99%80-%EC%88%9C%EC%84%9C-5c390b5323fa)

[hash cash]: http://www.hashcash.org/
