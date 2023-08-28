<template>
    <div>
        <div v-if="!gameStarted">
            <h1>Typing Game</h1>
            <button @click="startGame">Play</button>
        </div>
        <div v-else>
            <p>{{ currentSentence }}</p>
            <input v-model="inputText" @keyup.enter="checkInput" :disabled="gameEnded" placeholder="Enter Text"
                style="margin: 10px; font-size: 20px;">
            <p v-if="isCorrect">Correct!</p>
            <p v-else-if="isIncorrect">Wrong!</p>
            <div style="display: flex; flex-direction: column; align-items: center;">
                <button v-if="!gameEnded" @click="nextSentence">Next Sentence</button>
                <button v-else @click="restartGame">Play Again</button>
                <button v-if="gameEnded" @click="exitGame">Exit</button>
            </div>
            <div>
                <p v-if="gameEnded">Score: {{ getFormattedTime(currentTime) }}</p>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    data() {
        return {
            sentences: [],
            currentSentenceIndex: 0,
            currentSentence: '',
            inputText: '',
            isCorrect: false,
            isIncorrect: false,
            currentTime: 0,
            gameStarted: false,
            gameEnded: false,
            errorOccurred: false,
        };
    },
    mounted() {
        fetch('http://127.0.0.1:8000/rows')
            .then(response => response.json())
            .then(data => {
                this.sentences = data.rows;
            })
            .catch(error => {
                console.log(error);
                this.errorOccurred = true;
            });

        setInterval(() => {
            if (this.gameStarted && !this.gameEnded) {
                this.currentTime++;
            }
        }, 1000);
    },
    methods: {
        startGame() {
            this.gameStarted = true;
            this.currentSentenceIndex = 0;
            this.currentSentence = this.sentences[this.currentSentenceIndex].row_data;
            this.inputText = '';
            this.isCorrect = false;
            this.isIncorrect = false;
            this.currentTime = 0;
            this.gameEnded = false;
            this.errorOccurred = false;
        },
        exitGame() {
            this.gameStarted = false;
            this.gameEnded = false;
            this.inputText = '';
            this.currentSentenceIndex = 0;
            this.currentSentence = '';
            this.isCorrect = false;
            this.isIncorrect = false;
            this.currentTime = 0;
            this.errorOccurred = false;
        },
        checkInput() {
            if (this.inputText === this.currentSentence) {
                this.isCorrect = true;
                this.isIncorrect = false;
                this.nextSentence();
            } else {
                this.isCorrect = false;
                this.isIncorrect = true;
            }
        },
        nextSentence() {
            this.currentSentenceIndex++;
            if (this.currentSentenceIndex < this.sentences.length) {
                this.currentSentence = this.sentences[this.currentSentenceIndex].row_data;
                this.inputText = '';
                this.isCorrect = false;
                this.isIncorrect = false;
                if (!isNaN(this.sentences[this.currentSentenceIndex].time_to_next)) {
                    this.currentTime += this.sentences[this.currentSentenceIndex].time_to_next;
                }
            } else {
                this.gameEnded = true;
            }
        },
        restartGame() {
            this.startGame();
        },
        getFormattedTime(seconds) {
            if (isNaN(seconds)) {
                return "00:00";
            }
            const minutes = Math.floor(seconds / 60);
            const remainingSeconds = seconds % 60;
            return `${minutes}:${remainingSeconds < 10 ? '0' : ''}${remainingSeconds}`;
        },
    },
};
</script>