# FAHIMTA-NATLAS-TEST-001 — Human Evaluation Record

**Record status:** Human-reviewed, with provenance limitations  
**Evaluation date:** 2026-10-10  
**Input:** `Menene ake nufi da gwagwarmaya?`  
**Intended system:** N-ATLaS  
**Observed source:** Screenshot of a public N-ATLaS-branded demonstration interface  
**Score:** **3/5 — Adequate**  
**Determination:** **PASS WITH LIMITATIONS**

## 1. Standard Hausa reference answer

> Gwagwarmaya ita ce ƙoƙari ko fafutukar fuskantar wahala, kalubale, zalunci, ko rashin adalci domin cimma manufa, samun nasara, kare haƙƙi, samun ƴanci, ko kawo sauyi a rayuwa ko al’umma. Tana iya zama ta mutum ɗaya, kamar ƙoƙarin samun ilimi ko neman aiki; ko kuma ta jama’a, kamar fafutukar neman adalci, ƴanci, ko inganta yanayin zamantakewa.
>
> Gwagwarmaya na iya amfani da hanyoyi daban-daban, kamar himma da ƙoƙari, ilimi, magana da shawara, juriya, zanga-zanga, ko kare kai. Ba ta ƙuntata ga fada ko yaƙi ba. Hakanan, ma’anarta na iya zama mai kyau ko mara kyau dangane da manufar da ake bi da hanyar da ake bi wajen cimma ta.

## 2. English gloss

Gwagwarmaya is effort or struggle to confront hardship, challenges, oppression, or injustice in order to achieve a goal, succeed, defend rights, gain freedom, or bring change to life or society. It can be individual, such as striving for education or employment, or collective, such as advocacy for justice, freedom, or social improvement.

It may use different means—determination, education, dialogue and negotiation, resilience, protest, or self-defense—and is not limited to fighting or war. Its moral meaning can be positive or negative depending on the purpose and the methods used.

## 3. Captured response

> Gwagwarmaya na nufin kokarin fuskantar kalubale ko wahala ta hanyar amfani da karfi, himma, da dabaru daban-daban don samun nasara ko ci gaba. Ana yawan amfani da shi ne lokacin da mutum ke son karya wani abu mai wahala ko kuma ya doke abokin hamayya. Kalmar tana dauke da ma’anoni masu kyau da marasa kyau, dangane da sakamakon da burin da aka sa a gaba.

## 4. Human assessment

The captured response is broadly correct but semantically narrow. It identifies effort, determination, strategy, overcoming difficulty, and the possibility of positive or negative meaning. However, the examples “karya wani abu mai wahala” and “ya doke abokin hamayya” emphasize breaking something or defeating an opponent, risking a primarily confrontational framing.

The response omits important senses involving advocacy for rights, justice, freedom, social change, and collective struggle. Its explanation is therefore narrower than the established reference concept.

## 5. Reference dimensions

- **General meaning:** Sustained effort, struggle, or striving against difficulty or for a goal.
- **Goal orientation:** Success, progress, rights, freedom, justice, or change.
- **Individual and collective scope:** Personal effort or collective social/political action.
- **Means, not only force:** Determination, patience, strategy, education, advocacy, or peaceful resistance—not merely physical force.
- **Contextual valence:** Positive or negative depending on the aim and methods.
- **Natural Hausa phrasing:** Appropriate use of terms such as ƙoƙari, fafutaka, juriya, neman canji, and kare haƙƙi.

## 6. Score and decision

**Score: 3/5 — Adequate.** The core meaning is present, but the explanation omits several important dimensions in the reference.

**Determination: PASS WITH LIMITATIONS.** This is a qualitative human judgement for this test case only. It is not a statistically validated benchmark result and must not be generalized to overall model performance.

The reference material's separate “4 — Strong” label is not the score assigned to the captured response; the recorded response score remains 3/5.

## 7. Diagnostic tags

`semantic-narrowing`; `confrontation-overemphasis`; `omitted-collective-scope`; `omitted-rights-and-social-change`; `non-force-methods-underrepresented`.

## 8. Evidence and provenance limitations

- The screenshot supports that the prompt and response appeared in a public N-ATLaS-branded interface.
- The screenshot alone does **not** verify the exact backend model ID/revision, generation settings, or direct execution through FAHIMTA.
- The reference answer is the project's established human-review reference for this test. Further Hausa-language reviewer validation is recommended before formal benchmark use.
- The score is qualitative and case-specific. No aggregate accuracy, statistical significance, model superiority, or improvement claim is supported by this single case.

## 9. Follow-up actions

1. Preserve the original screenshot and raw response as evidence E-01; record capture date if known.
2. Verify the demo backend model ID/revision and generation settings where possible.
3. Re-run this case through a verified FAHIMTA–N-ATLaS execution path and record configuration and timestamp.
4. Apply the same reference and rubric consistently to future runs.
5. Compare before/after outputs only after a documented intervention; make no improvement claim without comparable evidence.

## 10. Project status impact

This result adds one documented, human-reviewed Hausa test case and a standard reference answer to FAHIMTA's research evidence. It does **not** mean the evaluator is implemented, direct model integration is verified, or the wider benchmark is complete.
