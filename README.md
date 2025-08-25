# 北京大学校规校纪
## 这是什么
北京大学校规校纪测试答案，包括了
1. 《北京大学研究生手册（2025）》
2. 《北京大学国际学生留学指南(2025)》
的题库

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
1. 不保证任何题目和答案的正确性和时效性，请大家自行判断
2. 还缺失很多题目和答案，欢迎PR