# 北京大学校规校纪
## 如何获取答案
1. 随便做一下题目
2. 提交答案后，在浏览器控制台运行下面的代码，就可以获取到当前所有题目的正确答案了
```javascript
const questions = app.questions; // 题目数组
const logs = app.answerLog;
const result = questions.map(q => {
    const qid = q.id;
    const item = logs[qid];
    let answer = "";
    if (item) {
        if (item.isRight) {
            answer = item.answer;
        } else {
            // 如果 rightAnswer 不为空
            if (item.rightAnswer !== undefined && item.rightAnswer !== "") {
                answer = item.rightAnswer;
            } else {
                // rightAnswer 为空时，answer 为 isRight（即 false）
                answer = item.isRight;
            }
        }
    }
    return {
        id: qid,
        content: q.content,
        answer: answer
    };
});
console.log(result);

```
## 其它
欢迎PR