<template>
    <div id="app">
        <h1>#pollthetrump</h1>
        <div class="container">
        </div>
        <div class="container tweet" v-for="i in tweets">
            <div class="half">
                <div class="tweet-wrap">
                    <Tweet :id="i[0]" :options="{ cards: 'hidden', width: '100%'}"></Tweet>
                </div>
                <div class="rating-bar">
                    <div class="yay">{{100-getNay(i)}}% #yaythetrump</div>
                    <div class="nay" v-bind:style="{width: getNay(i)+'%'}">{{getNay(i)+'%'}} #naythetrump</div>
                </div>
            </div>
        </div>
    </div>
</template>

<script type="text/babel">

    export default {
        name: 'app',
        methods: {
            getNay(i){
                let a = parseInt(i[2])
                let b = parseInt(i[3])
                let s = (a+b);
                console.log(s)
                return ((b/s)*100).toFixed(0);
            }
        },
        data () {
            return {
                msg: 'Welcome to Your Vue.js App',
                c: 0,
                tweets: [
                    ['847924397180583937', '2096', '640', '473', '0.5310'],
                    ['847895524632129536', '444', '132', '102', '0.5270'],
                    ['847878820220858369', '1014', '390', '248', '0.6292'],
                    ['847867380562894848', '339', '57', '57', '0.3363'],
                    ['847863243200753666', '443', '147', '87', '0.5282'],
                    ['847819720418111488', '149', '46', '23', '0.4631'],
                    ['847766558520856578', '1201', '306', '344', '0.5412'],
                    ['847625389908217856', '232', '85', '43', '0.5517'],
                    ['847573358912974849', '54', '20', '11', '0.5741'],
                    ['847573220417044480', '125', '31', '35', '0.5280'],
                    ['847559519085379584', '45', '12', '5', '0.3778'],
                    ['847559239149158401', '78', '27', '17', '0.5641'],
                    ['847558426557337600', '21', '6', '5', '0.5238'],
                    ['847455180912181249', '125', '41', '37', '0.6240'],
                    ['847435163143454723', '129', '40', '26', '0.5116'],
                    ['847270189171228672', '31', '8', '7', '0.4839'],
                    ['847236476815511552', '45', '12', '6', '0.4000'],
                    ['847061031293779969', '116', '31', '34', '0.5603'],
                    ['847056211006631936', '30', '8', '10', '0.6000'],
                    ['846854703183020032', '37', '13', '11', '0.6486'],
                    ['846841493952319489', '26', '8', '6', '0.5385'],
                    ['846672219073863681', '21', '9', '3', '0.5714'],
                    ['846533818811080704', '35', '5', '11', '0.4571'],
                ]
            }
        },
        mounted(){
            console.log('ready')
        }
    }
</script>

<style lang="scss" type="text/scss">
    #app {
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
        margin-top: 60px;
    }

    .tweet-wrap{
        max-width: 520px;
        margin: 0 auto;
    }

    .rating-bar {
        display: flex;
        max-width: 520px;
        margin: 0 auto;
        height: 20px;
        color: white;
        line-height: 40px;
        .yay {
            flex: 1;
            background-color: #E91D0E;
            height: 40px;
        }
        .nay {
            background-color: #232066;
            height: 40px;
        }
    }

    .tweet {
        min-height: 300px;
        border-bottom: 1px solid #ddd;
        .half {
            text-align: center;
            margin-left: 10px;
            padding: 10px;
        }
    }

    .container {

        max-width: 1200px;
        display: flex;
        margin: 0 auto;
        .half {
            margin: 20px;
            width: 100%;
            &.middle {
                align-content: center;
            }
            h2 {
                text-align: center;
                display: block;
            }
        }
    }

    h1, h2 {
        font-weight: normal;
    }

    ul {
        list-style-type: none;
        padding: 0;
    }

    li {
        display: inline-block;
        margin: 0 10px;
    }

    a {
        color: #42b983;
    }
</style>
