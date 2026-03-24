1. Import dictionary file (zip file in link below)
https://github.com/hoangdang1357/kanji_dic_viet_and_eng.git
2. Import my customized Senren notetype
https://github.com/hoangdang1357/current_senren.git
3. configure yomitan like this
![[Pasted image 20251123161212.png]]


4. Configure handlebars templates in yomitan
Append these lines (don't delete others)
```handlebars
{{#*inline "kanji_meaning"}}
    {{~#each definition.glossary~}}{{this}}{{#unless @last}}, {{/unless}}{{~/each~}}
{{/inline}}


{{#*inline "vietnamese"}}
    {{~#scope~}}
        {{~set "found" false~}}
        {{~#each definition.stats.misc~}}
            {{~#if (op "===" name "vietnamese")~}}
                {{~set "found" true~}}
                {{value}}
            {{~/if~}}
        {{~/each~}}
        {{~#if (op "!" (get "found"))~}}
            vietnamese: Unknown
        {{~/if~}}
    {{~/scope~}}
{{/inline}}


{{#*inline "jlpt"}}
    {{~#scope~}}
        {{~set "found" false~}}
        {{~#each definition.stats.misc~}}
            {{~#if (op "===" name "jlpt")~}}
                {{~set "found" true~}}
                {{value}}
            {{~/if~}}
        {{~/each~}}
        {{~#if (op "!" (get "found"))~}}
            JLPT: Unknown
        {{~/if~}}
    {{~/scope~}}
{{/inline}}

{{#*inline "grade"}}
    {{~#scope~}}
        {{~set "found" false~}}
        {{~#each definition.stats.misc~}}
            {{~#if (op "===" name "grade")~}}
                {{~set "found" true~}}
                {{value}}
            {{~/if~}}
        {{~/each~}}
        {{~#if (op "!" (get "found"))~}}
            Grade: Unknown
        {{~/if~}}
    {{~/scope~}}
{{/inline}}

{{#*inline "freq"}}
    {{~#scope~}}
        {{~set "found" false~}}
        {{~#each definition.stats.misc~}}
            {{~#if (op "===" name "freq")~}}
                {{~set "found" true~}}
                {{value}}
            {{~/if~}}
        {{~/each~}}
        {{~#if (op "!" (get "found"))~}}
            Frequency: Unknown
        {{~/if~}}
    {{~/scope~}}
{{/inline}}

{{#*inline "strokes"}}
    {{~#scope~}}
        {{~set "found" false~}}
        {{~#each definition.stats.misc~}}
            {{~#if (op "===" name "strokes")~}}
                {{~set "found" true~}}
                {{value}}
            {{~/if~}}
        {{~/each~}}
        {{~#if (op "!" (get "found"))~}}
            Strokes: Unknown
        {{~/if~}}
    {{~/scope~}}
{{/inline}}

```


