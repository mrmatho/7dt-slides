<template>
    <div class="slidev-layout">
        <div class="my-auto grid grid-cols-2 gap-4">
            <div class="border border-gray-400 ring-0 p-4 rounded-lg ">
                <h1 class="text-2xl pt-2 text-green-600"> Learning Intentions</h1>
                <slot name="li" />
            </div>
            <div class="border border-gray-400 ring-0 p-4 rounded-lg">
                <h1 class="text-2xl pt-2 text-indigo-600">Success Criteria</h1>
                <h4 class="text-xs text-gray-600 pb-2 italic">By the end of this lesson, students will be able to:</h4>
                <slot name="sc" />
            </div>
        </div>
    </div>
</template>
