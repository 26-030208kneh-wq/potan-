import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="폭탄 돌리기",
    page_icon="💣",
    layout="centered"
)

components.html(
r"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">

<style>

* {
    box-sizing: border-box;
}

body {
    margin: 0;
    background: #f3f5f7;
    font-family: Arial, sans-serif;
}

#app {
    width: 100%;
    max-width: 680px;
    margin: auto;
    text-align: center;
}


/* =========================
   제목
   ========================= */

.title {
    font-size: 42px;
    font-weight: bold;
    color: #252525;
    margin-top: 15px;
}

.subtitle {
    color: #777;
    margin-bottom: 25px;
}


/* =========================
   시작 화면
   ========================= */

.start-box {
    background: white;
    border-radius: 20px;
    padding: 30px;

    box-shadow:
        0 5px 20px rgba(0,0,0,.1);
}

.big-bomb {
    font-size: 75px;
    margin-bottom: 10px;
}

.start-title {
    font-size: 28px;
    font-weight: bold;
    color: #222;
}

.start-text {
    color: #777;
    margin: 10px 0 25px;
}

.start-button {
    width: 100%;

    border: none;
    border-radius: 12px;

    padding: 16px;
    margin: 8px 0;

    color: white;

    font-size: 18px;
    font-weight: bold;

    cursor: pointer;
}

.ai-button {
    background: #e53935;
}

.friend-button {
    background: #1976d2;
}


/* =========================
   인원 선택
   ========================= */

.player-select {
    display: none;

    background: white;

    border-radius: 20px;

    padding: 25px;

    margin-top: 15px;

    box-shadow:
        0 5px 20px rgba(0,0,0,.08);
}

.player-select-title {
    font-size: 22px;
    font-weight: bold;
    margin-bottom: 15px;
}

.player-number {
    width: 100%;

    padding: 13px;

    margin: 5px 0;

    border: 2px solid #ddd;

    border-radius: 10px;

    background: white;

    font-size: 17px;

    cursor: pointer;
}

.player-number:hover {
    background: #f1f1f1;
}


/* =========================
   게임
   ========================= */

#game {
    display: none;
}

.info {
    background: white;

    border-radius: 15px;

    padding: 15px;

    margin: 15px 0;

    box-shadow:
        0 3px 12px rgba(0,0,0,.08);
}

.turn {
    font-size: 19px;
    font-weight: bold;
}

.round {
    color: #777;
    margin-top: 5px;
}


/* =========================
   플레이어
   ========================= */

.players {
    display: grid;

    grid-template-columns:
        repeat(2, 1fr);

    gap: 10px;

    margin-top: 15px;
}

.player {
    background: white;

    border-radius: 15px;

    padding: 15px;

    box-shadow:
        0 3px 10px rgba(0,0,0,.08);

    transition: .2s;
}

.active {
    border: 3px solid #ffca28;

    transform: scale(1.03);

    box-shadow:
        0 0 15px rgba(255,193,7,.45);
}

.eliminated {
    opacity: .4;
    background: #ddd;
}

.player-icon {
    font-size: 38px;
}

.player-name {
    font-size: 17px;
    font-weight: bold;
    margin-top: 5px;
}

.status {
    margin-top: 5px;
    color: #777;
}


/* =========================
   폭탄 영역
   ========================= */

.bomb-area {
    background: #222;

    border-radius: 20px;

    padding: 30px 20px;

    margin-top: 20px;

    color: white;
}

.bomb {
    font-size: 100px;

    display: inline-block;

    animation:
        shake .7s infinite;
}

@keyframes shake {

    0% {
        transform: rotate(-4deg);
    }

    50% {
        transform: rotate(4deg);
    }

    100% {
        transform: rotate(-4deg);
    }

}

.timer {
    font-size: 42px;

    font-weight: bold;

    color: #ff5252;

    margin-top: 10px;
}

.timer.safe {
    color: #4caf50;
}

.timer.warning {
    color: #ffca28;
}

.timer.danger {
    color: #ff1744;

    animation:
        blink .5s infinite;
}

@keyframes blink {

    0% {
        opacity: 1;
    }

    50% {
        opacity: .3;
    }

    100% {
        opacity: 1;
    }

}


/* =========================
   폭탄 버튼
   ========================= */

.bomb-button {
    width: 100%;

    border: none;

    border-radius: 15px;

    padding: 20px;

    margin-top: 20px;

    background:
        linear-gradient(
            135deg,
            #ff1744,
            #d50000
        );

    color: white;

    font-size: 23px;

    font-weight: bold;

    cursor: pointer;

    box-shadow:
        0 5px 0 #8b0000;
}

.bomb-button:hover {
    transform: translateY(-2px);
}

.bomb-button:active {
    transform: translateY(3px);

    box-shadow:
        0 2px 0 #8b0000;
}

.bomb-button:disabled {
    opacity: .5;
    cursor: not-allowed;
}


/* =========================
   버튼
   ========================= */

.buttons {
    display: flex;

    gap: 10px;

    margin-top: 20px;
}

.game-button {
    flex: 1;

    border: none;

    border-radius: 10px;

    padding: 14px;

    font-size: 16px;

    font-weight: bold;

    cursor: pointer;
}

.restart {
    background: #168447;
    color: white;
}

.home {
    background: #555;
    color: white;
}


/* =========================
   결과
   ========================= */

.result {
    display: none;

    background: white;

    margin-top: 20px;

    padding: 25px;

    border-radius: 15px;

    font-size: 24px;

    font-weight: bold;

    box-shadow:
        0 4px 15px rgba(0,0,0,.12);
}

.result button {
    margin-top: 15px;

    border: none;

    border-radius: 10px;

    padding: 14px 30px;

    background: #168447;

    color: white;

    font-size: 18px;

    font-weight: bold;

    cursor: pointer;
}


/* =========================
   폭발
   ========================= */

.explosion {
    animation:
        explode .4s infinite;
}

@keyframes explode {

    0% {
        transform: scale(1);
    }

    50% {
        transform: scale(1.3);
    }

    100% {
        transform: scale(1);
    }

}


/* =========================
   모바일
   ========================= */

@media (max-width: 500px) {

    .title {
        font-size: 34px;
    }

    .players {
        grid-template-columns:
            repeat(2, 1fr);
    }

    .bomb {
        font-size: 80px;
    }

    .bomb-button {
        font-size: 20px;
    }

}

</style>
</head>


<body>

<div id="app">


<!-- ==================================================
     메인 화면
     ================================================== -->

<div id="home">

    <div class="title">
        💣 폭탄 돌리기
    </div>

    <div class="subtitle">
        폭탄이 터지기 전에 다음 사람에게 넘기세요!
    </div>


    <div class="start-box">

        <div class="big-bomb">
            💣
        </div>

        <div class="start-title">
            게임을 시작하세요
        </div>

        <div class="start-text">
            게임 방식을 선택해주세요.
        </div>


        <button
            class="start-button ai-button"
            onclick="startAI()"
        >
            🤖 AI와 하기
            <br>
            <small>
                나 1명 + AI 4명
            </small>
        </button>


        <button
            class="start-button friend-button"
            onclick="showFriendSelect()"
        >
            👥 친구와 하기
        </button>

    </div>


    <!-- 친구 인원 선택 -->

    <div
        class="player-select"
        id="playerSelect"
    >

        <div class="player-select-title">
            👥 인원수를 선택하세요
        </div>


        <button
            class="player-number"
            onclick="startFriend(2)"
        >
            2명
        </button>


        <button
            class="player-number"
            onclick="startFriend(3)"
        >
            3명
        </button>


        <button
            class="player-number"
            onclick="startFriend(4)"
        >
            4명
        </button>


        <button
            class="player-number"
            onclick="startFriend(5)"
        >
            5명
        </button>

    </div>

</div>


<!-- ==================================================
     게임 화면
     ================================================== -->

<div id="game">

    <div class="title">
        💣 폭탄 돌리기
    </div>


    <div class="info">

        <div
            class="turn"
            id="turnText"
        >
            플레이어 1의 차례
        </div>

        <div
            class="round"
            id="roundText"
        >
            라운드 1
        </div>

    </div>


    <!-- 플레이어 -->

    <div
        class="players"
        id="players"
    ></div>


    <!-- 폭탄 -->

    <div class="bomb-area">

        <div
            class="bomb"
            id="bomb"
        >
            💣
        </div>


        <div
            class="timer safe"
            id="timer"
        >
            30초
        </div>


        <button
            class="bomb-button"
            id="bombButton"
            onclick="passBomb()"
        >
            💣 폭탄 돌리기
        </button>

    </div>


    <!-- 결과 -->

    <div
        class="result"
        id="result"
    ></div>


    <!-- 버튼 -->

    <div class="buttons">

        <button
            class="game-button restart"
            onclick="restartGame()"
        >
            🔄 다시 시작
        </button>


        <button
            class="game-button home"
            onclick="goHome()"
        >
            🏠 처음으로
        </button>

    </div>

</div>

</div>


<script>

/* ==================================================
   게임 변수
   ================================================== */


/*
   최대 5명
*/

let players = [];


/*
   현재 플레이어
*/

let currentIndex = 0;


/*
   AI / 친구
*/

let gameMode = "ai";


*
   게임 종료 여부
*/

let gameOver = false;


/*
   라운드
*/

let round = 1;


/*
   ★ 핵심 ★

   게임 전체의 폭탄 시간.

   처음에는 30초.

   턴이 넘어가도 절대
   30초로 초기화하지 않는다.
*/

let remainingTime = 30;


/*
   타이머
*/

let timerInterval = null;


/*
   AI 타이머
*/

let aiTimeout = null;


/*
   폭발 처리 타이머
*/

let explosionTimeout = null;


/* ==================================================
   AI 게임 시작
   ================================================== */

function startAI() {

    gameMode = "ai";

    players = [];


    /*
       사람 1명
    */

    players.push({
        name: "나",
        type: "human",
        alive: true
    });


    /*
       AI 4명
    */

    for (
        let i = 1;
        i <= 4;
        i++
    ) {

        players.push({
            name: "AI " + i,
            type: "ai",
            alive: true
        });

    }


    document.getElementById(
        "home"
    ).style.display = "none";


    document.getElementById(
        "game"
    ).style.display = "block";


    restartGame();

}


/* ==================================================
   친구 선택 화면
   ================================================== */

function showFriendSelect() {

    const select =
        document.getElementById(
            "playerSelect"
        );


    if (
        select.style.display === "block"
    ) {

        select.style.display = "none";

    }

    else {

        select.style.display = "block";

    }

}


/* ==================================================
   친구 게임 시작
   ================================================== */

function startFriend(count) {

    gameMode = "friend";

    players = [];


    for (
        let i = 1;
        i <= count;
        i++
    ) {

        players.push({

            name:
                "플레이어 " + i,

            type:
                "human",

            alive:
                true

        });

    }


    document.getElementById(
        "home"
    ).style.display = "none";


    document.getElementById(
        "game"
    ).style.display = "block";


    restartGame();

}


/* ==================================================
   게임 초기화
   ================================================== */

function restartGame() {

    /*
       기존 타이머 제거
    */

    clearInterval(
        timerInterval
    );

    clearTimeout(
        aiTimeout
    );

    clearTimeout(
        explosionTimeout
    );


    /*
       혹시 플레이어가 없는 경우
    */

    if (
        players.length === 0
    ) {

        startAI();

        return;

    }


    /*
       모든 플레이어 생존
    */

    for (
        const player of players
    ) {

        player.alive = true;

    }


    /*
       첫 번째 플레이어부터
    */

    currentIndex = 0;


    /*
       첫 라운드
    */

    round = 1;


    /*
       ★ 항상 새 게임 시작 시
       30초부터 시작
    */

    remainingTime = 30;


    gameOver = false;


    /*
       폭탄 복구
    */

    const bomb =
        document.getElementById(
            "bomb"
        );


    bomb.textContent = "💣";

    bomb.classList.remove(
        "explosion"
    );


    /*
       버튼 활성화
    */

    document.getElementById(
        "bombButton"
    ).disabled = false;


    /*
       결과창 숨김
    */

    document.getElementById(
        "result"
    ).style.display = "none";


    /*
       화면 업데이트
    */

    renderPlayers();

    updateTurn();


    /*
       타이머 시작
    */

    startTimer();


    /*
       AI 확인
    */

    checkAI();

}


/* ==================================================
   플레이어 화면
   ================================================== */

function renderPlayers() {

    const container =
        document.getElementById(
            "players"
        );


    container.innerHTML = "";


    for (
        let i = 0;
        i < players.length;
        i++
    ) {

        const player =
            players[i];


        const div =
            document.createElement(
                "div"
            );


        div.className =
            "player";


        /*
           현재 플레이어
        */

        if (
            i === currentIndex &&
            player.alive
        ) {

            div.classList.add(
                "active"
            );

        }


        /*
           탈락
        */

        if (
            !player.alive
        ) {

            div.classList.add(
                "eliminated"
            );

        }


        /*
           아이콘
        */

        const icon =
            player.type === "ai"
            ? "🤖"
            : "👤";


        div.innerHTML =

            '<div class="player-icon">' +
            icon +
            '</div>' +

            '<div class="player-name">' +
            player.name +
            '</div>' +

            '<div class="status">' +

            (
                player.alive
                ? "🟢 생존"
                : "💀 탈락"
            ) +

            '</div>';


        container.appendChild(
            div
        );

    }

}


/* ==================================================
   차례 표시
   ================================================== */

function updateTurn() {

    const player =
        players[currentIndex];


    const text =
        document.getElementById(
            "turnText"
        );


    if (
        gameMode === "ai" &&
        player.type === "ai"
    ) {

        text.textContent =
            "🤖 " +
            player.name +
            "의 차례";

    }

    else {

        text.textContent =
            "👉 " +
            player.name +
            "의 차례";

    }


    document.getElementById(
        "roundText"
    ).textContent =
        "라운드 " +
        round;


    /*
       사람/AI에 따라 버튼 표시
    */

    const button =
        document.getElementById(
            "bombButton"
        );


    if (
        player.type === "ai"
    ) {

        button.textContent =
            "🤖 AI가 폭탄을 돌리는 중...";

    }

    else {

        button.textContent =
            "💣 폭탄 돌리기";

    }

}


/* ==================================================
   ★ 전체 게임 타이머
   ================================================== */

function startTimer() {

    /*
       기존 인터벌 제거

       중요:
       시간을 초기화하지 않는다.
    */

    clearInterval(
        timerInterval
    );


    /*
       현재 남은 시간 표시
    */

    updateTimerDisplay();


    /*
       1초마다 감소
    */

    timerInterval =
        setInterval(
            function() {

                if (gameOver) {

                    clearInterval(
                        timerInterval
                    );

                    return;

                }


                remainingTime--;


                updateTimerDisplay();


                /*
                   0초
                */

                if (
                    remainingTime <= 0
                ) {

                    remainingTime = 0;


                    clearInterval(
                        timerInterval
                    );


                    explode();

                }

            },
            1000
        );

}


/* ==================================================
   타이머 표시
   ================================================== */

function updateTimerDisplay() {

    const timer =
        document.getElementById(
            "timer"
        );


    timer.textContent =
        remainingTime + "초";


    /*
       색상 변경
    */

    timer.classList.remove(
        "safe",
        "warning",
        "danger"
    );


    if (
        remainingTime > 15
    ) {

        timer.classList.add(
            "safe"
        );

    }

    else if (
        remainingTime > 7
    ) {

        timer.classList.add(
            "warning"
        );

    }

    else {

        timer.classList.add(
            "danger"
        );

    }

}


/* ==================================================
   ★ 폭탄 돌리기
   ================================================== */

function passBomb() {

    if (gameOver) {

        return;

    }


    /*
       현재 플레이어
    */

    const player =
        players[currentIndex];


    /*
       폭탄 돌리기 버튼을 누른 순간
       현재 턴 종료
    */

    /*
       타이머는 절대 초기화하지 않는다.
    */


    /*
       AI 타이머가 있다면 취소
    */

    clearTimeout(
        aiTimeout
    );


    /*
       다음 플레이어
    */

    nextPlayer();

}


/* ==================================================
   다음 생존 플레이어
   ================================================== */

function nextPlayer() {

    let next =
        currentIndex;


    let attempts = 0;


    do {

        next =
            (next + 1) %
            players.length;


        attempts++;

    }
    while (
        !players[next].alive &&
        attempts <
        players.length + 1
    );


    currentIndex = next;


    /*
       라운드 증가
    */

    round++;


    /*
       화면 갱신
    */

    renderPlayers();

    updateTurn();


    /*
       ★ 중요 ★

       여기서는 타이머를 새로 시작하지 않는다.

       게임 전체에서 하나의 타이머가
       계속 감소하도록 한다.
    */


    checkAI();

}


/* ==================================================
   AI
   ================================================== */

function checkAI() {

    if (gameOver) {

        return;

    }


    const player =
        players[currentIndex];


    /*
       AI 차례인지 확인
    */

    if (
        gameMode === "ai" &&
        player.type === "ai" &&
        player.alive
    ) {

        clearTimeout(
            aiTimeout
        );


        /*
           ★ AI 빠르게 ★

           0.4 ~ 0.9초
        */

        const delay =
            400 +
            Math.random() * 500;


        aiTimeout =
            setTimeout(
                function() {

                    /*
                       게임이 끝났는지 다시 확인
                    */

                    if (
                        gameOver
                    ) {

                        return;

                    }


                    /*
                       AI도 폭탄 돌리기 버튼을
                       누르는 것과 같은 동작
                    */

                    passBomb();

                },
                delay
            );

    }

}


/* ==================================================
   폭발
   ================================================== */

function explode() {

    if (gameOver) {

        return;

    }


    /*
       모든 타이머 정지
    */

    clearInterval(
        timerInterval
    );


    clearTimeout(
        aiTimeout
    );


    /*
       폭탄 폭발 표시
    */

    const bomb =
        document.getElementById(
            "bomb"
        );


    bomb.textContent =
        "💥";


    bomb.classList.add(
        "explosion"
    );


    /*
       현재 플레이어
       탈락
    */

    const player =
        players[currentIndex];


    player.alive = false;


    /*
       화면 갱신
    */

    renderPlayers();


    document.getElementById(
        "turnText"
    ).textContent =
        "💥 " +
        player.name +
        " 탈락!";


    /*
       폭발 후 잠시 대기
    */

    explosionTimeout =
        setTimeout(
            function() {

                bomb.classList.remove(
                    "explosion"
                );


                bomb.textContent =
                    "💣";


                /*
                   생존자
                */

                const alive =
                    players.filter(
                        p => p.alive
                    );


                /*
                   마지막 1명
                */

                if (
                    alive.length <= 1
                ) {

                    if (
                        alive.length === 1
                    ) {

                        finishGame(
                            "🏆 " +
                            alive[0].name +
                            " 승리!"
                        );

                    }

                    else {

                        finishGame(
                            "🤝 무승부!"
                        );

                    }


                    return;

                }


                /*
                   다음 생존자 찾기
                */

                let next =
                    currentIndex;


                do {

                    next =
                        (next + 1) %
                        players.length;

                }
                while (
                    !players[next].alive
                );


                currentIndex =
                    next;


                round++;


                /*
                   화면 갱신
                */

                renderPlayers();

                updateTurn();


                /*
                   ★ 중요 ★

                   여기에서도 타이머를
                   30초로 초기화하지 않는다.

                   남은 시간 그대로 계속된다.
                */

                startTimer();


                checkAI();

            },
            1200
        );

}


/* ==================================================
   게임 종료
   ================================================== */

function finishGame(message) {

    gameOver = true;


    clearInterval(
        timerInterval
    );


    clearTimeout(
        aiTimeout
    );


    clearTimeout(
        explosionTimeout
    );


    document.getElementById(
        "bombButton"
    ).disabled = true;


    const result =
        document.getElementById(
            "result"
        );


    result.style.display =
        "block";


    result.innerHTML =

        message +

        "<br><br>" +

        '<button onclick="goHome()">' +

        "🔄 다시하기" +

        "</button>";


    setTimeout(
        function() {

            result.scrollIntoView({
                behavior: "smooth",
                block: "center"
            });

        },
        100
    );

}


/* ==================================================
   메인 화면
   ================================================== */

function goHome() {

    /*
       타이머 정지
    */

    clearInterval(
        timerInterval
    );


    clearTimeout(
        aiTimeout
    );


    clearTimeout(
        explosionTimeout
    );


    gameOver = false;


    /*
       게임 숨기기
    */

    document.getElementById(
        "game"
    ).style.display =
        "none";


    /*
       메인 화면
    */

    document.getElementById(
        "home"
    ).style.display =
        "block";


    /*
       결과 숨기기
    */

    document.getElementById(
        "result"
    ).style.display =
        "none";


    /*
       인원 선택 숨기기
    */

    document.getElementById(
        "playerSelect"
    ).style.display =
        "none";

}

</script>

</body>
</html>
""",
    height=1100,
    scrolling=True
)
