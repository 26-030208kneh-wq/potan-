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
   메인 화면
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
   폭탄
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
    font-size: 34px;
    font-weight: bold;

    color: #ff5252;

    margin-top: 10px;
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


/* =========================
   게임 버튼
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
        explode .5s infinite;
}

@keyframes explode {

    0% {
        transform: scale(1);
    }

    50% {
        transform: scale(1.25);
    }

    100% {
        transform: scale(1);
    }

}

</style>
</head>


<body>

<div id="app">


<!-- =================================
     메인 화면
     ================================= -->

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


<!-- =================================
     게임 화면
     ================================= -->

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
            class="timer"
            id="timer"
        >
            준비!
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


    <!-- 아래 버튼 -->

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

/* =========================================
   기본 설정
   ========================================= */

let players = [];

let currentIndex = 0;

let gameMode = "ai";

let gameOver = false;

let round = 1;

let bombTime = 10;

let timerInterval = null;

let aiTimeout = null;


/* =========================================
   AI 시작
   ========================================= */

function startAI() {

    gameMode = "ai";

    players = [];


    /* 사람 */

    players.push({
        name: "나",
        type: "human",
        alive: true
    });


    /* AI 4명 */

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


/* =========================================
   친구 인원 선택
   ========================================= */

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


/* =========================================
   친구 게임 시작
   ========================================= */

function startFriend(count) {

    gameMode = "friend";

    players = [];


    for (
        let i = 1;
        i <= count;
        i++
    ) {

        players.push({
            name: "플레이어 " + i,
            type: "human",
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


/* =========================================
   게임 초기화
   ========================================= */

function restartGame() {

    clearInterval(timerInterval);

    clearTimeout(aiTimeout);


    /* 플레이어가 없을 경우 */

    if (
        players.length === 0
    ) {

        startAI();

        return;

    }


    for (
        const player of players
    ) {

        player.alive = true;

    }


    currentIndex = 0;

    round = 1;

    gameOver = false;


    document.getElementById(
        "result"
    ).style.display = "none";


    document.getElementById(
        "bomb"
    ).classList.remove(
        "explosion"
    );


    document.getElementById(
        "bombButton"
    ).disabled = false;


    renderPlayers();

    updateTurn();

    startTimer();

    checkAI();

}


/* =========================================
   플레이어 화면
   ========================================= */

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


        if (
            i === currentIndex &&
            player.alive
        ) {

            div.classList.add(
                "active"
            );

        }


        if (
            !player.alive
        ) {

            div.classList.add(
                "eliminated"
            );

        }


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


/* =========================================
   현재 차례
   ========================================= */

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

}


/* =========================================
   타이머
   ========================================= */

function startTimer() {

    clearInterval(timerInterval);


    /*
       폭탄 제한시간은
       매 턴마다 랜덤
    */

    bombTime =
        Math.floor(
            Math.random() * 7
        ) + 5;


    let remaining =
        bombTime;


    document.getElementById(
        "timer"
    ).textContent =
        remaining + "초";


    timerInterval =
        setInterval(
            function() {

                if (gameOver) {

                    clearInterval(
                        timerInterval
                    );

                    return;

                }


                remaining--;


                document.getElementById(
                    "timer"
                ).textContent =
                    remaining + "초";


                if (
                    remaining <= 0
                ) {

                    clearInterval(
                        timerInterval
                    );


                    explode();

                }

            },
            1000
        );

}


/* =========================================
   폭탄 돌리기
   ========================================= */

function passBomb() {

    if (gameOver) {

        return;

    }


    const player =
        players[currentIndex];


    /*
       현재 플레이어만
       버튼을 누를 수 있음
    */

    /*
       버튼을 눌렀다는 것은
       폭탄이 터지기 전에
       다음 사람에게 넘긴 것
    */


    clearInterval(
        timerInterval
    );


    nextPlayer();

}


/* =========================================
   다음 플레이어
   ========================================= */

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
        attempts < players.length + 1
    );


    currentIndex = next;


    /* 한 바퀴 돌면 라운드 증가 */

    round++;


    renderPlayers();

    updateTurn();

    startTimer();

    checkAI();

}


/* =========================================
   AI 자동 버튼
   ========================================= */

function checkAI() {

    if (gameOver) {

        return;

    }


    const player =
        players[currentIndex];


    if (
        gameMode === "ai" &&
        player.type === "ai" &&
        player.alive
    ) {

        clearTimeout(aiTimeout);


        /*
           AI도 실제로
           폭탄 돌리기 버튼을 누르는 것처럼
           약간 기다린 후 실행
        */

        aiTimeout =
            setTimeout(
                function() {

                    passBomb();

                },
                1200 +
                Math.random() * 1800
            );

    }

}


/* =========================================
   폭발
   ========================================= */

function explode() {

    if (gameOver) {

        return;

    }


    clearInterval(
        timerInterval
    );


    clearTimeout(
        aiTimeout
    );


    const bomb =
        document.getElementById(
            "bomb"
        );


    bomb.textContent =
        "💥";


    bomb.classList.add(
        "explosion"
    );


    const player =
        players[currentIndex];


    /*
       현재 플레이어 탈락
    */

    player.alive = false;


    renderPlayers();


    document.getElementById(
        "turnText"
    ).textContent =
        "💥 " +
        player.name +
        " 탈락!";


    /*
       1.5초 후 다음 단계
    */

    setTimeout(
        function() {

            bomb.classList.remove(
                "explosion"
            );


            bomb.textContent =
                "💣";


            /* 생존자 수 */

            const alive =
                players.filter(
                    p => p.alive
                );


            /* 마지막 한 명 */

            if (
                alive.length <= 1
            ) {

                finishGame(
                    alive.length === 1
                    ? "🏆 " +
                      alive[0].name +
                      " 승리!"
                    : "🤝 무승부!"
                );

                return;

            }


            /*
               탈락한 사람 다음부터
               차례 시작
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


            renderPlayers();

            updateTurn();

            startTimer();

            checkAI();

        },
        1500
    );

}


/* =========================================
   게임 종료
   ========================================= */

function finishGame(message) {

    gameOver = true;


    clearInterval(
        timerInterval
    );


    clearTimeout(
        aiTimeout
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


/* =========================================
   메인 화면
   ========================================= */

function goHome() {

    clearInterval(
        timerInterval
    );


    clearTimeout(
        aiTimeout
    );


    gameOver = false;


    document.getElementById(
        "game"
    ).style.display =
        "none";


    document.getElementById(
        "home"
    ).style.display =
        "block";


    document.getElementById(
        "result"
    ).style.display =
        "none";


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
